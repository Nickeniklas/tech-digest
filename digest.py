import os
import re
import json
import datetime
from pathlib import Path

import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from concurrent.futures import ThreadPoolExecutor
import logging

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

logging.basicConfig(
    filename="digest.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

MODEL     = "claude-haiku-4-5-20251001"

MAX_CONTEXT_CHARS = 16_000

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; tech-digest-bot/1.0)"}

# ---------------------------------------------------------------------------
# Digest generation prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """
You are writing a daily AI and tech news digest for professionals who are curious about AI but don't have a technical background. Think: teachers, marketers, lawyers, designers, managers — people who use AI tools and want to stay informed, but don't write code for a living.

Your job is to make today's most important stories clear, relevant, and worth reading in under 5 minutes.

## Reader brief

The reader is smart and busy. They follow AI news because it affects their work, not because they love technology for its own sake. They don't need jargon explained at length — just one plain sentence, then move on. They want to know what happened and why it matters to them personally.

## Voice & tone

Write like a calm, clear journalist who knows tech well. Confident but not opinionated. Informative but never dry.

- Never hype: no "groundbreaking", "revolutionary", "game-changer", "exciting"
- No passive corporate tone: never "it has been announced that..."
- No padding, no filler transitions, no hedging
- When something is technical: one plain-language sentence, then move on
- Talk directly to the reader using "you"
- Never make the reader feel behind for not knowing something

## Structure

Produce exactly three sections:

### 1. lead_story
The single most important or interesting AI/tech story today. Explain what happened in plain language. Include a "what_this_means" field written for a general professional audience. If the story has obvious relevance to specific professions (e.g. teachers, lawyers, marketers), mention them naturally — never force it. Max ~150 words total across all fields.

### 2. quick_hits
3–4 shorter stories. Each one is 2–3 sentences max. No jargon. Just what happened and why it matters. These should be fast to read.

### 3. under_the_hood
1–2 more technical stories for readers who want to go deeper. Still written in plain language, but can include more detail. If there is a simple, runnable code example (max 10 lines of Python), include it. This section is clearly marked as the nerdy part — readers self-select into it.

## Visuals

For each story, consider whether a visual would help:
- If the story involves data, numbers, comparisons, or benchmarks → suggest a chart or table (set visual_type to "chart" or "table" and provide the data in visual_data)
- If the story is about a product, tool, or announcement → provide an image URL if one is available in the source material (set visual_type to "image" and visual_url to the URL)
- If no visual adds value → set visual_type to null

## Story selection

Use ONLY the provided headlines — never invent or assume stories.

Prioritise:
- Real releases and shipped features over announcements and demos
- Stories with clear real-world impact over purely technical ones
- Freshness — skip anything older than 48 hours unless truly significant

Skip: funding rounds, corporate drama, vague announcements, rumours.

## Deduplication

A list of recently covered topics may be provided. Skip any story that is the same topic with no meaningful new development. Meaningful new development includes: a new release, major update, reversal, significant new data, or a follow-up announcement. If a follow-up is warranted, begin what_happened with: "Previously covered on {date}: [brief recap]. Since then, ..."

## Output format — IMPORTANT

Output ONLY a JSON block using these exact delimiters:

<!-- BEGIN_JSON -->
{
  "teaser": "One sentence. What's the most interesting thing today — written for a curious non-technical reader.",
  "fun_fact": null,
  "lead_story": {
    "title": "Story title",
    "what_happened": "1–2 sentences. Plain language. What actually happened.",
    "what_this_means": "1–2 sentences. Why does this matter? Generic professional audience. Include profession examples if obvious.",
    "visual_type": "image | chart | table | null",
    "visual_url": "https://... or null",
    "visual_data": null,
    "source_name": "Source Name",
    "source_url": "https://..."
  },
  "quick_hits": [
    {
      "title": "Story title",
      "summary": "2–3 sentences max. What happened and why it matters. No jargon.",
      "visual_type": null,
      "visual_url": null,
      "visual_data": null,
      "source_name": "Source Name",
      "source_url": "https://..."
    }
  ],
  "under_the_hood": [
    {
      "title": "Story title",
      "what_happened": "Plain language but more detail than quick hits.",
      "why_it_matters": "Technical significance. Who this is for.",
      "code_example": null,
      "visual_type": "chart | table | null",
      "visual_url": null,
      "visual_data": null,
      "source_name": "Source Name",
      "source_url": "https://..."
    }
  ]
}
<!-- END_JSON -->

### Field rules
- "fun_fact": one punchy sentence if genuinely interesting — otherwise null. Max 20 words.
- "visual_type": exactly "image", "chart", "table", or null
- "visual_url": only use URLs from provided source material — never fabricate
- "visual_data": for charts/tables, provide a JSON object with keys "headers" and "rows"
- "code_example": plain text only, no markdown fences, max 10 lines — under_the_hood only
- "teaser": written for a non-technical reader, no jargon
- Output valid JSON — no trailing commas, no comments
""".strip()

# ---------------------------------------------------------------------------
# Web fetching & extraction
# ---------------------------------------------------------------------------

_PRIVATE_PREFIXES = (
    "http://localhost", "https://localhost",
    "http://127.", "https://127.",
    "http://10.", "https://10.",
    "http://192.168.", "https://192.168.",
    "http://169.254.", "https://169.254.",
)


def fetch_page(url: str) -> str:
    try:
        r = requests.get(url, timeout=12, headers=HEADERS)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  [warn] Could not fetch {url}: {e}")
        logging.info(f"  [warn] Could not fetch {url}: {e}")
        return ""


def fetch_article_detail(url: str) -> dict:
    """Fetch one article page and extract og:image URL + first real paragraph."""
    if not url.startswith(("http://", "https://")):
        return {}
    if any(url.startswith(p) for p in _PRIVATE_PREFIXES):
        return {}
    try:
        r = requests.get(url, timeout=8, headers=HEADERS)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        image_url = None
        for prop in ("og:image", "twitter:image"):
            tag = soup.find("meta", property=prop) or soup.find("meta", attrs={"name": prop})
            if tag and tag.get("content", "").startswith("http"):
                image_url = tag["content"]
                break

        body = ""
        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if len(text) >= 80:
                body = text[:300]
                break

        return {"image_url": image_url, "body": body}
    except Exception:
        return {}


def enrich_items(items: list[dict], source: str, n: int = 3) -> list[dict]:
    """Fetch article detail for the first n items in parallel and merge results."""
    targets = items[:n]
    urls = [item["url"] for item in targets]
    with ThreadPoolExecutor(max_workers=8) as executor:
        details = list(executor.map(fetch_article_detail, urls))
    for item, detail in zip(targets, details):
        item.update(detail)
    n_img  = sum(1 for d in details if d.get("image_url"))
    n_body = sum(1 for d in details if d.get("body"))
    print(f"    {source}: {n_img} image(s), {n_body} body(s) from {len(targets)} articles")
    logging.info(f"Enriched {source}: {n_img} images, {n_body} bodies")
    return items


def extract_hn(html: str) -> list[dict]:
    """Hacker News front page — title + URL for top 30 stories."""
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for row in soup.select("tr.athing")[:30]:
        a = row.select_one("span.titleline > a")
        if a:
            items.append({"title": a.get_text(strip=True), "url": a.get("href", "")})
    return items


def extract_github_trending(html: str) -> list[dict]:
    """GitHub trending — repo name + URL + short description."""
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for article in soup.select("article.Box-row")[:20]:
        h2 = article.select_one("h2 a")
        desc_el = article.select_one("p")
        if h2:
            name = " ".join(h2.get_text().split())
            url  = "https://github.com" + h2.get("href", "")
            desc = desc_el.get_text(strip=True)[:250] if desc_el else ""
            items.append({"title": name, "url": url, "description": desc})
    return items


def extract_generic(html: str, base_url: str = "") -> list[dict]:
    """
    Generic extractor for blog/news pages.
    Grabs article titles + links from common patterns (h2 a, h3 a, article a).
    """
    soup = BeautifulSoup(html, "html.parser")
    seen_urls = set()
    items = []

    for tag in ("h2", "h3", "h1"):
        for el in soup.find_all(tag):
            a = el.find("a", href=True)
            if not a:
                continue
            title = a.get_text(strip=True)
            href  = a["href"]
            if not href.startswith("http"):
                href = base_url.rstrip("/") + "/" + href.lstrip("/")
            if not title or href in seen_urls:
                continue
            seen_urls.add(href)
            # Look for a sibling/nearby <p> for a short description
            desc = ""
            parent = el.parent
            if parent:
                p = parent.find("p")
                if p:
                    desc = p.get_text(strip=True)[:250]
            items.append({"title": title, "url": href, "description": desc})
            if len(items) >= 20:
                break
        if items:
            break

    return items


def format_section(name: str, items: list[dict]) -> str:
    if not items:
        return ""
    lines = [f"\n### {name}"]
    for item in items:
        line = f"- {item['title']} — {item['url']}"
        if item.get("description"):
            line += f"\n  {item['description']}"
        if item.get("body"):
            line += f"\n  Body: {item['body']}"
        if item.get("image_url"):
            line += f"\n  Image: {item['image_url']}"
        lines.append(line)
    return "\n".join(lines)


def gather_context() -> str:
    """Fetch all sources and return a trimmed context string."""
    print("  Fetching Hacker News...")
    hn_items = extract_hn(fetch_page("https://news.ycombinator.com"))

    print("  Fetching GitHub Trending...")
    gh_items = extract_github_trending(fetch_page("https://github.com/trending"))

    print("  Fetching HuggingFace Blog...")
    hf_items = extract_generic(fetch_page("https://huggingface.co/blog"), "https://huggingface.co")

    print("  Fetching Anthropic News...")
    ant_items = extract_generic(fetch_page("https://anthropic.com/news"), "https://anthropic.com")

    print("  Fetching GitHub Blog...")
    ghb_items = extract_generic(fetch_page("https://github.blog"), "https://github.blog")

    # Enrich top articles from trusted blog sources with og:image + first paragraph.
    # HN and GitHub Trending are skipped: HN links arbitrary external sites (prompt
    # injection risk), Trending links repo pages (no useful og:image or article body).
    # OpenAI removed: their /news page returns 403 reliably; HN surfaces OpenAI news anyway.
    print("  Enriching blog articles...")
    enrich_items(hf_items,  "HuggingFace", n=3)
    enrich_items(ant_items, "Anthropic",   n=3)
    enrich_items(ghb_items, "GitHub Blog", n=3)

    sections = [
        format_section("Hacker News", hn_items),
        format_section("GitHub Trending", gh_items),
        format_section("HuggingFace Blog", hf_items),
        format_section("Anthropic News", ant_items),
        format_section("GitHub Blog", ghb_items),
    ]

    context = "\n".join(s for s in sections if s)

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS] + "\n\n[truncated]"

    return context


# ---------------------------------------------------------------------------
# Seen-topics deduplication
# ---------------------------------------------------------------------------

SEEN_TOPICS_PATH = Path(__file__).parent / "seen_topics.json"


def load_seen_topics() -> list[dict]:
    """Load seen_topics.json and prune entries older than 7 days."""
    if not SEEN_TOPICS_PATH.exists():
        return []
    try:
        entries = json.loads(SEEN_TOPICS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    cutoff = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()
    return [e for e in entries if e.get("date", "") >= cutoff]


def format_seen_topics_context(seen: list[dict]) -> str:
    """Format seen topics into a context block for the Claude user message."""
    if not seen:
        return ""
    lines = ["Previously covered topics (last 7 days — skip unless there is meaningful new development):"]
    for e in seen:
        urls = ", ".join(e.get("source_urls", []))
        lines.append(f"{e['date']} | {e['title']} | {e['summary']} | {urls}")
    return "\n".join(lines)


def extract_seen_entries(data: dict, date_str: str) -> list[dict]:
    """Build seen_topics entries from today's generated digest."""
    entries = []

    def _entry(title: str, raw_text: str, source_url: str) -> dict:
        first_sentence = raw_text.split(".")[0].strip()
        summary = first_sentence + "." if first_sentence else raw_text[:120]
        return {"date": date_str, "title": title, "summary": summary, "source_urls": [source_url]}

    lead = data.get("lead_story", {})
    if lead:
        entries.append(_entry(lead["title"], lead.get("what_happened", ""), lead["source_url"]))

    for story in data.get("quick_hits", []):
        entries.append(_entry(story["title"], story.get("summary", ""), story["source_url"]))

    for story in data.get("under_the_hood", []):
        entries.append(_entry(story["title"], story.get("what_happened", ""), story["source_url"]))

    return entries


def save_seen_topics(seen: list[dict], new_entries: list[dict]) -> None:
    """Merge, re-prune, and write seen_topics.json."""
    combined = seen + new_entries
    cutoff = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()
    combined = [e for e in combined if e.get("date", "") >= cutoff]
    SEEN_TOPICS_PATH.write_text(json.dumps(combined, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Claude call
# ---------------------------------------------------------------------------

def generate_digest(date_str: str, context: str, seen_topics: list[dict]) -> str:
    seen_block = format_seen_topics_context(seen_topics)
    user_msg = f"Today's date is {date_str}.\n\n"
    if seen_block:
        user_msg += seen_block + "\n\n"
    user_msg += f"Here are today's headlines from key tech sources:\n\n{context}\n\nGenerate the digest."

    client = anthropic.Anthropic(timeout=120)
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=3500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
        return response.content[0].text
    except Exception as e:
        raise RuntimeError(f"Anthropic API call failed: {e}")

# ---------------------------------------------------------------------------
# Output handling
# ---------------------------------------------------------------------------

_MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def _md_links_to_html(text: str) -> str:
    """Convert markdown inline links [text](url) to HTML anchor tags."""
    return _MD_LINK_RE.sub(
        lambda m: f'<a href="{m.group(2)}" style="color:inherit;text-decoration:underline;">{m.group(1)}</a>',
        text,
    )


def _chart_bars(visual_data: dict) -> list[dict]:
    """Convert visual_data to {label, value, pct} dicts for bar chart rendering."""
    if not visual_data or not visual_data.get("rows"):
        return []
    rows = visual_data["rows"]
    try:
        vals = [float(row[1]) for row in rows if len(row) > 1]
        max_val = max(vals) if vals else 1
        result = []
        for row in rows:
            val = float(row[1]) if len(row) > 1 else 0
            pct = int(val / max_val * 100) if max_val else 0
            result.append({"label": row[0], "value": row[1], "pct": pct})
        return result
    except (ValueError, TypeError):
        return [{"label": row[0], "value": row[1] if len(row) > 1 else "", "pct": 50} for row in rows]


def render_markdown(data: dict, full_date: str) -> str:
    lines = [
        f"# Daily Tech Digest — {full_date}", "",
        f"> {data['teaser']}", "",
        "---",
    ]

    lead = data["lead_story"]
    lines += [
        f"## {lead['title']}", "",
        "**What happened**", lead["what_happened"], "",
        "**What this means**", lead["what_this_means"], "",
        f"Source: [{lead['source_name']} ↗]({lead['source_url']})", "",
        "---",
    ]

    quick_hits = data.get("quick_hits", [])
    if quick_hits:
        lines += ["## Quick Hits", ""]
        for story in quick_hits:
            lines += [
                f"### {story['title']}", "",
                story["summary"], "",
                f"Source: [{story['source_name']} ↗]({story['source_url']})", "",
            ]
        lines.append("---")

    under = data.get("under_the_hood", [])
    if under:
        lines += ["## Under the Hood", ""]
        for story in under:
            lines += [
                f"### {story['title']}", "",
                "**What happened**", story["what_happened"], "",
                "**Why it matters**", story["why_it_matters"], "",
            ]
            if story.get("code_example"):
                lines += [f"```python\n{story['code_example']}\n```", ""]
            lines += [f"Source: [{story['source_name']} ↗]({story['source_url']})", ""]
        lines.append("---")

    if data.get("fun_fact"):
        lines += [f"**Fun fact:** {data['fun_fact']}", ""]

    lines.append("*Daily tech digest for curious professionals. AI news that affects your work.*")
    return "\n".join(lines)


def render_html(data: dict, full_date: str) -> str:
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)))
    env.filters["md_links"] = _md_links_to_html
    env.filters["chart_bars"] = _chart_bars
    template = env.get_template("template.html")
    return template.render(full_date=full_date, **data)


def parse_output(text: str) -> dict:
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_response.txt").write_text(text, encoding="utf-8")

    json_match = re.search(r"<!-- BEGIN_JSON -->(.*?)<!-- END_JSON -->", text, re.DOTALL)
    if not json_match:
        raise ValueError("Could not find <!-- BEGIN_JSON --> block. See digests/raw_response.txt.")

    return json.loads(json_match.group(1).strip())


def save_files(date_str: str, md: str, html: str) -> tuple[Path, Path]:
    os.makedirs("digests", exist_ok=True)
    md_path   = Path(f"digests/tech-digest-{date_str}.md")
    html_path = Path(f"digests/tech-digest-{date_str}.html")
    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html, encoding="utf-8")
    return md_path, html_path


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    load_dotenv()

    today     = datetime.date.today()
    date_str  = today.strftime("%Y-%m-%d")
    full_date = today.strftime("%A, %B %d %Y").replace(" 0", " ")

    # Skip if today's digest already exists (to avoid duplicates on reruns)
    if Path(f"digests/tech-digest-{date_str}.html").exists():
        print(f"Digest for {date_str} already generated, skipping.")
        logging.info(f"Digest for {date_str} already exists, skipping.")
        return

    seen_topics = load_seen_topics()
    logging.info(f"Loaded {len(seen_topics)} seen topic(s) from last 7 days")

    print(f"Gathering headlines for {date_str}...")
    logging.info(f"Starting digest generation for {date_str}")
    context = gather_context()
    print(f"  Context size: {len(context):,} chars")
    logging.info(f"Context gathered with {len(context):,} chars")
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_context.txt").write_text(context, encoding="utf-8")

    print("Generating digest...")
    logging.info("Calling Anthropic API...")  # <-- if script hangs, log stops here
    raw = generate_digest(date_str, context, seen_topics)
    logging.info("Anthropic API call completed")  # <-- confirms API didn't hang

    print("Parsing output...")
    data = parse_output(raw)

    print("Rendering...")
    md   = render_markdown(data, full_date)
    html = render_html(data, full_date)

    print("Saving files...")
    save_files(date_str, md, html)
    print(f"  -> digests/tech-digest-{date_str}.md")
    print(f"  -> digests/tech-digest-{date_str}.html")
    logging.info(f"Files saved for {date_str}")

    new_entries = extract_seen_entries(data, date_str)
    save_seen_topics(seen_topics, new_entries)
    logging.info(f"seen_topics.json updated with {len(new_entries)} new entry(ies)")

    print(f"Done. Digest saved for {date_str}.")
    logging.info(f"Digest generation completed for {date_str}")


if __name__ == "__main__":
    main()
