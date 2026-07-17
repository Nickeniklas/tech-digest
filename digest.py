import os
import re
import json
import datetime
from html import escape
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

load_dotenv()

MODEL     = os.environ.get("DIGEST_MODEL", "claude-haiku-4-5-20251001")
BASE_URL  = os.environ.get("DIGEST_BASE_URL")

MAX_CONTEXT_CHARS = 16_000

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; tech-digest-bot/1.0)"}

# ---------------------------------------------------------------------------
# Digest generation prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (Path(__file__).parent / "prompts" / "system_prompt.md").read_text(encoding="utf-8").strip()

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
    except requests.exceptions.HTTPError as e:
        # x-deny-reason distinguishes a proxy denial (routine env allowlist) from
        # a block by the origin server itself, which look identical as bare 403s.
        resp = getattr(e, "response", None)
        if resp is None:
            detail = str(e)
        else:
            detail = f"HTTP {resp.status_code}"
            deny_reason = resp.headers.get("x-deny-reason")
            if deny_reason:
                detail += f" (x-deny-reason: {deny_reason})"
        print(f"  [warn] Could not fetch {url}: {detail}")
        logging.warning(f"  [warn] Could not fetch {url}: {detail}")
        return ""
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
    Grabs article titles + links from common patterns. Handles both the
    heading-wraps-anchor pattern (``<h2><a>Title</a></h2>``) and the
    anchor-wraps-heading card pattern (``<a href><h2>Title</h2></a>``, used by
    HuggingFace's blog since mid-2026).
    """
    soup = BeautifulSoup(html, "html.parser")
    seen_urls = set()
    items = []

    for tag in ("h2", "h3", "h1"):
        for el in soup.find_all(tag):
            # Anchor inside the heading, or a heading wrapped by an anchor card.
            a = el.find("a", href=True) or el.find_parent("a", href=True)
            if not a:
                continue
            # Prefer the heading's own text — an ancestor anchor may wrap extra
            # markup (image, byline) whose text would pollute the title.
            title = el.get_text(strip=True) or a.get_text(strip=True)
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


def gather_context() -> tuple[str, str, set[str]]:
    """Fetch all sources and return (context_string, image_refs_block, known_urls)."""
    print("  Fetching Hacker News...")
    hn_items = extract_hn(fetch_page("https://news.ycombinator.com"))

    print("  Fetching GitHub Trending...")
    gh_items = extract_github_trending(fetch_page("https://github.com/trending"))

    print("  Fetching HuggingFace Blog...")
    hf_items = extract_generic(fetch_page("https://huggingface.co/blog"), "https://huggingface.co")

    print("  Fetching Anthropic News...")
    ant_items = extract_generic(fetch_page("https://www.anthropic.com/news"), "https://www.anthropic.com")

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

    # Fail-loud guardrail: count how many sources returned usable content.
    # A 403/empty fetch yields an empty item list, so an empty list == failure.
    # We refuse to build a digest from partial data rather than emit a hollow one.
    sources = [
        ("Hacker News", hn_items),
        ("GitHub Trending", gh_items),
        ("HuggingFace Blog", hf_items),
        ("Anthropic News", ant_items),
        ("GitHub Blog", ghb_items),
    ]
    succeeded = [name for name, items in sources if items]
    failed    = [name for name, items in sources if not items]
    for name in failed:
        print(f"  [warn] {name} returned no usable content (403 / empty / parse failure)")
        logging.warning(f"{name} returned no usable content (403 / empty / parse failure)")

    MIN_SOURCES = 3
    if len(succeeded) < MIN_SOURCES:
        msg = (
            f"Only {len(succeeded)}/{len(sources)} sources returned content "
            f"(failed: {', '.join(failed) or 'none'}) — aborting; refusing to "
            f"build a digest from partial data."
        )
        logging.error(msg)
        raise RuntimeError(msg)

    sections = [format_section(name, items) for name, items in sources]
    context = "\n".join(s for s in sections if s)

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS] + "\n\n[truncated]"

    # Build a compact image reference block so Claude can easily match image URLs to stories.
    image_lines = []
    for item in hf_items + ant_items + ghb_items:
        if item.get("image_url"):
            image_lines.append(f'  - "{item["title"]}": {item["image_url"]}')
    image_refs = ""
    if image_lines:
        image_refs = "Available image URLs (use these verbatim for matching stories — do not use any other URLs):\n" + "\n".join(image_lines)

    # URLs we actually fetched ourselves — the only ones trusted as source_url/visual_url.
    # Claude's output is checked against this set before rendering, since the scraped
    # content it summarizes could otherwise be used to smuggle in an attacker-chosen URL.
    known_urls = set()
    for items in (hn_items, gh_items, hf_items, ant_items, ghb_items):
        for item in items:
            if item.get("url"):
                known_urls.add(item["url"])
            if item.get("image_url"):
                known_urls.add(item["image_url"])

    return context, image_refs, known_urls


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

    def _entry(story: dict, text_field: str) -> dict:
        raw_text = story.get(text_field) or ""
        first_sentence = raw_text.split(".")[0].strip()
        summary = first_sentence + "." if first_sentence else raw_text[:120]
        source_url = story.get("source_url")
        return {
            "date": date_str,
            "title": story.get("title", ""),
            "summary": summary,
            "source_urls": [source_url] if source_url else [],
        }

    lead = data.get("lead_story")
    if isinstance(lead, dict):
        entries.append(_entry(lead, "what_happened"))

    for story in data.get("quick_hits") or []:
        if isinstance(story, dict):
            entries.append(_entry(story, "summary"))

    for story in data.get("under_the_hood") or []:
        if isinstance(story, dict):
            entries.append(_entry(story, "what_happened"))

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

def generate_digest(date_str: str, context: str, seen_topics: list[dict], image_refs: str = "") -> str:
    seen_block = format_seen_topics_context(seen_topics)
    user_msg = f"Today's date is {date_str}.\n\n"
    if image_refs:
        user_msg += image_refs + "\n\n"
    if seen_block:
        user_msg += seen_block + "\n\n"
    user_msg += f"Here are today's headlines from key tech sources:\n\n{context}\n\nGenerate the digest."

    client_kwargs = {"timeout": 120}
    if BASE_URL:
        client_kwargs["base_url"] = BASE_URL
    client = anthropic.Anthropic(**client_kwargs)
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
    """Convert markdown inline links [text](url) to HTML anchor tags.

    The output of this function is rendered with the Jinja `| safe` filter, so it
    must do its own escaping. Only http(s) URLs become real links — anything else
    (e.g. a javascript: URI from a manipulated story) degrades to plain text.
    """
    parts = []
    last_end = 0
    for m in _MD_LINK_RE.finditer(text):
        parts.append(escape(text[last_end:m.start()]))
        link_text = escape(m.group(1))
        url = m.group(2)
        if url.startswith(("http://", "https://")):
            parts.append(
                f'<a href="{escape(url)}" style="color:inherit;text-decoration:underline;" '
                f'target="_blank" rel="noopener">{link_text}</a>'
            )
        else:
            parts.append(link_text)
        last_end = m.end()
    parts.append(escape(text[last_end:]))
    return "".join(parts)


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


def _source_line(story: dict) -> str:
    if story.get("source_url"):
        return f"Source: [{story['source_name']} ↗]({story['source_url']})"
    return f"Source: {story['source_name']}"


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
        _source_line(lead), "",
        "---",
    ]

    quick_hits = data.get("quick_hits", [])
    if quick_hits:
        lines += ["## Quick Hits", ""]
        for story in quick_hits:
            lines += [
                f"### {story['title']}", "",
                story["summary"], "",
                _source_line(story), "",
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
            lines += [_source_line(story), ""]
        lines.append("---")

    if data.get("fun_fact"):
        lines += [f"**Fun fact:** {data['fun_fact']}", ""]

    lines.append("*Daily tech digest for curious professionals. AI news that affects your work.*")
    return "\n".join(lines)


def render_html(data: dict, full_date: str) -> str:
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)), autoescape=True)
    env.filters["md_links"] = _md_links_to_html
    env.filters["chart_bars"] = _chart_bars
    template = env.get_template("template.html")
    return template.render(full_date=full_date, **data)


def build_archive_entries() -> list[dict]:
    entries = []
    for html_path in Path("digests").glob("tech-digest-*.html"):
        date_str = html_path.stem.removeprefix("tech-digest-")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        teaser = ""
        md_path = html_path.with_suffix(".md")
        if md_path.exists():
            for line in md_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("> "):
                    teaser = line[2:].strip()
                    break

        entries.append({
            "date": date_str,
            "full_date": date.strftime("%d %b %Y"),
            "teaser": teaser,
            "html_path": f"digests/{html_path.name}",
        })

    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def render_archive(entries: list[dict]) -> str:
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)), autoescape=True)
    template = env.get_template("archive_template.html")
    return template.render(entries=entries)


def parse_output(text: str) -> dict:
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_response.txt").write_text(text, encoding="utf-8")

    json_match = re.search(r"<!-- BEGIN_JSON -->(.*?)<!-- END_JSON -->", text, re.DOTALL)
    if not json_match:
        raise ValueError("Could not find <!-- BEGIN_JSON --> block. See digests/raw_response.txt.")

    return json.loads(json_match.group(1).strip())


def _is_trusted_url(url: str | None, known_urls: set[str]) -> bool:
    return bool(url) and url.startswith(("http://", "https://")) and url in known_urls


def sanitize_story_urls(data: dict, known_urls: set[str]) -> dict:
    """Drop any source_url/visual_url Claude returned that isn't one of the URLs we
    actually fetched. The system prompt instructs Claude to only use verbatim URLs
    from the supplied context, but that's a prompt instruction, not a safety
    boundary — scraped content could contain text designed to override it. This is
    the actual enforcement, checked before anything is ever rendered into HTML.
    """
    stories = [
        data.get("lead_story"),
        *(data.get("quick_hits") or []),
        *(data.get("under_the_hood") or []),
    ]
    for story in stories:
        if not isinstance(story, dict):
            continue
        if story.get("source_url") and not _is_trusted_url(story["source_url"], known_urls):
            logging.warning(f"Dropping unverified source_url: {story['source_url']!r}")
            story["source_url"] = None
        if story.get("visual_url") and not _is_trusted_url(story["visual_url"], known_urls):
            logging.warning(f"Dropping unverified visual_url: {story['visual_url']!r}")
            story["visual_url"] = None
    return data


def save_files(date_str: str, md: str, html: str) -> tuple[Path, Path]:
    os.makedirs("digests", exist_ok=True)
    md_path   = Path(f"digests/tech-digest-{date_str}.md")
    html_path = Path(f"digests/tech-digest-{date_str}.html")
    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html, encoding="utf-8")
    return md_path, html_path


# ---------------------------------------------------------------------------
# Pipeline stages (shared by `python digest.py`, `gather`, and `finish`)
# ---------------------------------------------------------------------------

BUILD_DIR = Path("build")


def update_index_html(date_str: str) -> None:
    """Rewrite index.html to redirect to today's digest."""
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=digests/tech-digest-{date_str}.html">
</head>
<body>
  <p>Redirecting to latest digest...</p>
</body>
</html>"""
    Path("index.html").write_text(html, encoding="utf-8")


def gather_stage() -> dict | None:
    """Load seen topics and fetch headlines. Returns None if today's digest
    already exists (nothing to do), otherwise a dict with everything needed
    to generate and finish today's digest.
    """
    today     = datetime.date.today()
    date_str  = today.strftime("%Y-%m-%d")
    full_date = today.strftime("%A, %B %d %Y").replace(" 0", " ")

    if Path(f"digests/tech-digest-{date_str}.html").exists():
        return None

    seen_topics = load_seen_topics()
    logging.info(f"Loaded {len(seen_topics)} seen topic(s) from last 7 days")
    seen_block = format_seen_topics_context(seen_topics)

    logging.info(f"Starting digest generation for {date_str}")
    context, image_refs, known_urls = gather_context()
    logging.info(f"Context gathered with {len(context):,} chars")

    return {
        "date_str": date_str,
        "full_date": full_date,
        "seen_topics": seen_topics,
        "seen_block": seen_block,
        "image_refs": image_refs,
        "context": context,
        "known_urls": known_urls,
    }


def finish_stage(date_str: str, full_date: str, raw: str, known_urls: set[str]) -> tuple[Path, Path]:
    """Parse, sanitize, render, save, and regenerate archive.html + index.html."""
    data = parse_output(raw)
    data = sanitize_story_urls(data, known_urls)

    md   = render_markdown(data, full_date)
    html = render_html(data, full_date)
    md_path, html_path = save_files(date_str, md, html)
    logging.info(f"Files saved for {date_str}")

    seen_topics = load_seen_topics()
    new_entries = extract_seen_entries(data, date_str)
    save_seen_topics(seen_topics, new_entries)
    logging.info(f"seen_topics.json updated with {len(new_entries)} new entry(ies)")

    archive_entries = build_archive_entries()
    Path("archive.html").write_text(render_archive(archive_entries), encoding="utf-8")
    logging.info(f"archive.html regenerated with {len(archive_entries)} entries")

    update_index_html(date_str)
    logging.info(f"index.html updated to redirect to {date_str}")

    return md_path, html_path


# ---------------------------------------------------------------------------
# CLI subcommands
# ---------------------------------------------------------------------------

def cmd_gather() -> None:
    gathered = gather_stage()
    if gathered is None:
        print("SKIP")
        return

    BUILD_DIR.mkdir(exist_ok=True)
    gather_output = (
        f"IMAGE_REFS:\n{gathered['image_refs']}\n\n"
        f"SEEN_BLOCK:\n{gathered['seen_block']}\n\n"
        f"CONTEXT:\n{gathered['context']}"
    )
    (BUILD_DIR / "gather_output.txt").write_text(gather_output, encoding="utf-8")
    (BUILD_DIR / "known_urls.txt").write_text(
        "\n".join(sorted(gathered["known_urls"])), encoding="utf-8"
    )

    print(f"PROCEED:{gathered['date_str']}")
    print(f"Context size: {len(gathered['context']):,} chars")


def cmd_finish(raw_path: str) -> None:
    today     = datetime.date.today()
    date_str  = today.strftime("%Y-%m-%d")
    full_date = today.strftime("%A, %B %d %Y").replace(" 0", " ")

    raw = Path(raw_path).read_text(encoding="utf-8")
    known_urls = set(
        line for line in (BUILD_DIR / "known_urls.txt").read_text(encoding="utf-8").splitlines() if line
    )

    md_path, html_path = finish_stage(date_str, full_date, raw, known_urls)
    print(f"  -> {md_path}")
    print(f"  -> {html_path}")
    print(f"  -> archive.html")
    print(f"  -> index.html")


def main() -> None:
    gathered = gather_stage()
    if gathered is None:
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        print(f"Digest for {date_str} already generated, skipping.")
        logging.info(f"Digest for {date_str} already exists, skipping.")
        return

    date_str   = gathered["date_str"]
    full_date  = gathered["full_date"]
    context    = gathered["context"]
    known_urls = gathered["known_urls"]

    print(f"Gathering headlines for {date_str}...")
    print(f"  Context size: {len(context):,} chars")
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_context.txt").write_text(context, encoding="utf-8")

    print("Generating digest...")
    logging.info("Calling Anthropic API...")  # <-- if script hangs, log stops here
    raw = generate_digest(date_str, context, gathered["seen_topics"], gathered["image_refs"])
    logging.info("Anthropic API call completed")  # <-- confirms API didn't hang

    print("Parsing, rendering, saving...")
    md_path, html_path = finish_stage(date_str, full_date, raw, known_urls)
    print(f"  -> {md_path}")
    print(f"  -> {html_path}")
    print(f"  -> archive.html")
    print(f"  -> index.html")

    print(f"Done. Digest saved for {date_str}.")
    logging.info(f"Digest generation completed for {date_str}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate the daily tech digest.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("gather", help="Fetch headlines and write build/gather_output.txt")

    finish_parser = subparsers.add_parser("finish", help="Render and save the digest from a raw response file")
    finish_parser.add_argument("raw_path", help="Path to the raw Claude output (e.g. build/digest_raw.txt)")

    args = parser.parse_args()

    if args.command == "gather":
        cmd_gather()
    elif args.command == "finish":
        cmd_finish(args.raw_path)
    else:
        main()
