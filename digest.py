import os
import re
import json
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import logging

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

logging.basicConfig(
    filename="digest.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

MODEL     = "claude-sonnet-4-6"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

MAX_CONTEXT_CHARS = 20_000

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; tech-digest-bot/1.0)"}

# ---------------------------------------------------------------------------
# Digest generation prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """
You are generating a daily tech digest for developers and AI-literate readers.
You will be given a pre-curated list of today's headlines from key tech sources.
Use ONLY the provided headlines — do not invent or assume additional stories.

### 1. Select the best 3–5 topics

Pick the most relevant, impactful, and practically useful stories.
Prioritise:
- Actionable updates (new APIs, features you can use today)
- Breaking changes or deprecations
- Genuinely new releases (not rumours or demos)

Skip: funding rounds, corporate drama, vague announcements, anything
older than 48 hours unless truly significant.

### 2. Voice & tone

Write as a sharp, senior developer who reads everything so the reader
doesn't have to. You have opinions — use them.

**Do:**
- Have a clear take on each story
- Talk directly to the reader using "you"
- Distinguish between shipped features and announcements/demos — call it
  out explicitly
- Be concise and confident — one strong sentence beats three hedging ones

**Never use:**
- Hype words: groundbreaking, revolutionary, exciting, game-changer,
  thrilled, proud
- Passive corporate tone: "it has been announced that..."
- Filler transitions: "In conclusion...", "It's worth noting that..."
- Unnecessary hedging: "This could potentially possibly..."

Dry wit is welcome, but never forced. If a story is boring, say so
briefly and move on.

**On technical depth:**
When a story is highly technical, open WHY IT MATTERS with one sentence
naming what the technology is — no deep explanation. Then pivot immediately
to real-world impact: why a non-specialist should care, what changes for
them, what is cool about it. Assume the reader will click the link to learn
more. Use your words to make them want to, not to replace the article.
Keep entries tight. One sharp sentence beats three explanatory ones.

### 3. Write each entry (Markdown format)

Use this adaptive format:

## [Topic Title] — [🤖 AI | 🛠️ Dev Tools | 💾 Hardware]

**WHAT HAPPENED**
1–2 sentences. Facts only, no hype. When you reference a product or tool
that has a URL in the provided headlines, linkify it inline:
[tool name](https://...). Only use URLs from the provided headlines.

**WHY IT MATTERS**
1–2 sentences. What does this change for the reader specifically? Same
inline link rule applies.

**[TRY IT / THE TAKE]**
- If actionable (new API, tool, command): minimal working example or
  exact command. Max 15 lines.
- If conceptual or not yet usable: 1–2 sentences of actual editorial
  opinion. What should the reader watch for?

↗ [Source name](URL)

Choosing between TRY IT and THE TAKE:
- New API with docs → TRY IT
- Model release accessible today → TRY IT
- Research paper or demo only → THE TAKE
- Deprecation or breaking change → THE TAKE
- Tool update with a new command → TRY IT

### 4. Assemble the Markdown document

# Daily Tech Digest — {Full date, e.g. Thursday, April 3 2026}

> {1 sentence teaser referencing today's lead story, written with a point of view}

**Today's pick:** {1–2 sentences on why you chose today's lead. What
makes it worth stopping for? Be direct — this is your editorial voice.}

---

{Lead story — same format, can run up to 300 words if warranted}

---

{Remaining 2–4 stories}

---
*Daily digest for developers. AI, dev tools, and the occasional hardware
drop that actually matters.*

How to pick the lead:
- Most actionable today
- Biggest shift in a space readers follow closely
- If two tie — pick the one with the better TRY IT example

### 5. Constraints
- 150–250 words per topic entry (aim for the lower end — concise wins)
- Readable in under 5 minutes
- Never fabricate news — only report what is in the provided headlines
- If a category has no meaningful news today, skip it
- Do not over-explain technical concepts — one orienting sentence maximum,
  then focus on real-world impact. The reader has the link.

### 6. Output format — IMPORTANT

At the very end of your response, output BOTH a structured JSON block and
the Markdown version using these exact delimiters:

<!-- BEGIN_JSON -->
{
  "teaser": "1-sentence teaser with point of view",
  "todays_pick": "1-2 sentence editorial note on the lead story",
  "stories": [
    {
      "title": "Story title",
      "category": "AI",
      "is_lead": true,
      "what_happened": "Facts. Can contain [text](url) inline links using URLs from the headlines.",
      "why_it_matters": "Impact. Can contain [text](url) inline links.",
      "action_type": "TRY IT",
      "action_is_code": true,
      "action_content": "pip install something\n# minimal example here",
      "source_name": "Source Name",
      "source_url": "https://..."
    }
  ]
}
<!-- END_JSON -->

<!-- BEGIN_MARKDOWN -->
{full markdown content}
<!-- END_MARKDOWN -->

JSON field rules:
- "category": must be exactly "AI", "Dev Tools", or "Hardware"
- "is_lead": true for exactly one story (the first/lead story), false for others
- "action_type": exactly "TRY IT" or "THE TAKE"
- "action_is_code": true if action_content is a code snippet, false if it is prose
- "action_content": for TRY IT code, plain code text only (no markdown fences);
  for THE TAKE, plain prose
- Inline links in what_happened/why_it_matters use standard Markdown syntax:
  [text](url) — only URLs actually present in the provided headlines
- Output valid JSON (no trailing commas, no comments inside the JSON block)
""".strip()

# ---------------------------------------------------------------------------
# Web fetching & extraction
# ---------------------------------------------------------------------------

def fetch_page(url: str) -> str:
    try:
        r = requests.get(url, timeout=12, headers=HEADERS)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  [warn] Could not fetch {url}: {e}")
        logging.info(f"  [warn] Could not fetch {url}: {e}")
        return ""


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
            desc = desc_el.get_text(strip=True)[:150] if desc_el else ""
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
                    desc = p.get_text(strip=True)[:150]
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

    print("  Fetching OpenAI News...")
    oai_items = extract_generic(fetch_page("https://openai.com/news"), "https://openai.com")

    print("  Fetching Anthropic News...")
    ant_items = extract_generic(fetch_page("https://anthropic.com/news"), "https://anthropic.com")

    print("  Fetching GitHub Blog...")
    ghb_items = extract_generic(fetch_page("https://github.blog"), "https://github.blog")

    sections = [
        format_section("Hacker News", hn_items),
        format_section("GitHub Trending", gh_items),
        format_section("HuggingFace Blog", hf_items),
        format_section("OpenAI News", oai_items),
        format_section("Anthropic News", ant_items),
        format_section("GitHub Blog", ghb_items),
    ]

    context = "\n".join(s for s in sections if s)

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS] + "\n\n[truncated]"

    return context


# ---------------------------------------------------------------------------
# Claude call
# ---------------------------------------------------------------------------

def generate_digest(date_str: str, context: str) -> str:
    client = anthropic.Anthropic(timeout=120)
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": (
                    f"Today's date is {date_str}.\n\n"
                    f"Here are today's headlines from key tech sources:\n\n"
                    f"{context}\n\n"
                    "Generate the digest."
                ),
            }],
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


def render_html(data: dict, full_date: str) -> str:
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)))
    env.filters["md_links"] = _md_links_to_html
    template = env.get_template("template.html")
    return template.render(full_date=full_date, **data)


def parse_output(text: str) -> tuple[dict, str]:
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_response.txt").write_text(text, encoding="utf-8")

    json_match = re.search(r"<!-- BEGIN_JSON -->(.*?)<!-- END_JSON -->", text, re.DOTALL)
    md_match   = re.search(r"<!-- BEGIN_MARKDOWN -->(.*?)<!-- END_MARKDOWN -->", text, re.DOTALL)

    if not json_match:
        raise ValueError("Could not find <!-- BEGIN_JSON --> block. See digests/raw_response.txt.")
    if not md_match:
        raise ValueError("Could not find <!-- BEGIN_MARKDOWN --> block. See digests/raw_response.txt.")

    data = json.loads(json_match.group(1).strip())
    return data, md_match.group(1).strip()


def save_files(date_str: str, md: str, html: str) -> tuple[Path, Path]:
    os.makedirs("digests", exist_ok=True)
    md_path   = Path(f"digests/tech-digest-{date_str}.md")
    html_path = Path(f"digests/tech-digest-{date_str}.html")
    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html, encoding="utf-8")
    return md_path, html_path


def send_email(date_str: str, full_date: str, html: str, md_path: Path, app_password: str) -> None:
    from_email = os.environ["MAIL_FROM"]
    to_email   = os.environ["MAIL_TO"]
    subject    = f"Daily Tech Digest — {full_date}"

    msg = MIMEMultipart("mixed")
    msg["From"]    = from_email
    msg["To"]      = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(html, "html", "utf-8"))

    md_attachment = MIMEText(md_path.read_text(encoding="utf-8"), "plain", "utf-8")
    md_attachment.add_header(
        "Content-Disposition",
        "attachment",
        filename=f"tech-digest-{date_str}.md",
    )
    msg.attach(md_attachment)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email, app_password)
        smtp.sendmail(from_email, to_email, msg.as_string())


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    load_dotenv()

    app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not app_password:
        raise EnvironmentError("GMAIL_APP_PASSWORD not set in .env")
    if not os.environ.get("MAIL_FROM") or not os.environ.get("MAIL_TO"):
        raise EnvironmentError("MAIL_FROM and MAIL_TO must be set in .env")

    today     = datetime.date.today()
    date_str  = today.strftime("%Y-%m-%d")
    full_date = today.strftime("%A, %B %d %Y").replace(" 0", " ")

    print(f"Gathering headlines for {date_str}...")
    logging.info(f"Starting digest generation for {date_str}")
    context = gather_context()
    print(f"  Context size: {len(context):,} chars")
    logging.info(f"Context gathered with {len(context):,} chars")

    print("Generating digest...")
    logging.info("Calling Anthropic API...")  # <-- if script hangs, log stops here
    raw = generate_digest(date_str, context)
    logging.info("Anthropic API call completed")  # <-- confirms API didn't hang

    print("Parsing output...")
    data, md = parse_output(raw)

    print("Rendering HTML...")
    html = render_html(data, full_date)

    print("Saving files...")
    md_path, _ = save_files(date_str, md, html)
    print(f"  → digests/tech-digest-{date_str}.md")
    print(f"  → digests/tech-digest-{date_str}.html")
    logging.info(f"Files saved for {date_str}")

    print("Sending email...")
    logging.info(f"Sending email for {date_str}")
    send_email(date_str, full_date, html, md_path, app_password)
    print(f"Done. Digest sent for {date_str}.")
    logging.info(f"Digest generation completed for {date_str}")


if __name__ == "__main__":
    main()
