import os
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

MODEL      = "claude-sonnet-4-6"
FROM_EMAIL = "savonheimoniklas@gmail.com"
TO_EMAIL   = "savonheimoniklas@gmail.com"
SMTP_HOST  = "smtp.gmail.com"
SMTP_PORT  = 587

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

### 3. Write each entry

Use this adaptive format:

## [Topic Title] — [🤖 AI | 🛠️ Dev Tools | 💾 Hardware]

**WHAT HAPPENED**
1–2 sentences. Facts only, no hype.

**WHY IT MATTERS**
1–2 sentences. What does this change for the reader specifically?

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

### 4. Assemble the document

# 🗞️ Daily Tech Digest — {Full date, e.g. Thursday, April 3 2026}

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

### 5. HTML email format

Generate a self-contained HTML file, all styles inline (no <style> blocks).
Max width 600px. Structure:

**Header:** background #0f0f0f, white title (22px, weight 600), muted date
line (11px uppercase), teaser in lighter gray below a subtle divider.

**Today's pick strip:** background #1a1a2e, 3px solid #534AB7 left border.
Small purple label "TODAY'S PICK" (11px uppercase, color #AFA9EC), editorial
note below in muted text (#c8c8d8, 13px).

**Content area:** white background, 0.5px border, rounded bottom corners
(10px). Stories separated by 0.5px horizontal rules.

**Each story entry:**
- Category badge: pill shape, inline with emoji
  - AI: background #EEEDFE, color #3C3489
  - Dev Tools: background #EAF3DE, color #27500A
  - Hardware: background #FEF3C7, color #92400E
- Title: 17px, font-weight 600
- Field labels (WHAT HAPPENED, WHY IT MATTERS, TRY IT, THE TAKE):
  12px, uppercase, letter-spacing 0.04em, muted color, own line above text
- Code blocks: background #1e1e1e, color #d4d4d4, font-family Menlo/
  Consolas/monospace, padding 14px, border-radius 8px
- Source link: ↗ Source name, color matches category badge

**Footer:** centered, 12px, muted — "Daily digest for developers. AI,
dev tools, and the occasional hardware drop that actually matters."

### 6. Constraints
- 150–250 words per topic entry
- Readable in under 5 minutes
- Never fabricate news — only report what is in the provided headlines
- If a category has no meaningful news today, skip it

### 7. Output format — IMPORTANT

At the very end of your response, output BOTH the Markdown and HTML versions
using these exact delimiters (nothing after the closing HTML delimiter):

<!-- BEGIN_MARKDOWN -->
{full markdown content}
<!-- END_MARKDOWN -->

<!-- BEGIN_HTML -->
{full self-contained HTML content}
<!-- END_HTML -->
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
    client = anthropic.Anthropic()
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


# ---------------------------------------------------------------------------
# Output handling
# ---------------------------------------------------------------------------

def parse_output(text: str) -> tuple[str, str]:
    os.makedirs("digests", exist_ok=True)
    Path("digests/raw_response.txt").write_text(text, encoding="utf-8")

    md_match   = re.search(r"<!-- BEGIN_MARKDOWN -->(.*?)<!-- END_MARKDOWN -->", text, re.DOTALL)
    html_match = re.search(r"<!-- BEGIN_HTML -->(.*?)<!-- END_HTML -->", text, re.DOTALL)

    if not md_match:
        raise ValueError("Could not find <!-- BEGIN_MARKDOWN --> block. See digests/raw_response.txt.")
    if not html_match:
        raise ValueError("Could not find <!-- BEGIN_HTML --> block. See digests/raw_response.txt.")

    return md_match.group(1).strip(), html_match.group(1).strip()


def save_files(date_str: str, md: str, html: str) -> tuple[Path, Path]:
    os.makedirs("digests", exist_ok=True)
    md_path   = Path(f"digests/tech-digest-{date_str}.md")
    html_path = Path(f"digests/tech-digest-{date_str}.html")
    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html, encoding="utf-8")
    return md_path, html_path


def send_email(date_str: str, full_date: str, html: str, md_path: Path, app_password: str) -> None:
    subject = f"🗞️ Daily Tech Digest — {full_date}"

    msg = MIMEMultipart("mixed")
    msg["From"]    = FROM_EMAIL
    msg["To"]      = TO_EMAIL
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
        smtp.login(FROM_EMAIL, app_password)
        smtp.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    load_dotenv()

    app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not app_password:
        raise EnvironmentError("GMAIL_APP_PASSWORD not set in .env")

    today     = datetime.date.today()
    date_str  = today.strftime("%Y-%m-%d")
    full_date = today.strftime("%A, %B %d %Y").replace(" 0", " ")

    print(f"Gathering headlines for {date_str}...")
    context = gather_context()
    print(f"  Context size: {len(context):,} chars")

    print("Generating digest...")
    raw = generate_digest(date_str, context)

    print("Parsing output...")
    md, html = parse_output(raw)

    print("Saving files...")
    md_path, _ = save_files(date_str, md, html)
    print(f"  → digests/tech-digest-{date_str}.md")
    print(f"  → digests/tech-digest-{date_str}.html")

    print("Sending email...")
    send_email(date_str, full_date, html, md_path, app_password)
    print(f"Done. Digest sent for {date_str}.")


if __name__ == "__main__":
    main()
