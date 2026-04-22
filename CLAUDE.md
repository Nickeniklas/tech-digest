# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Tech Digest — Project Instructions

## What this project does
Generates a daily tech news digest for developers, saves it as HTML and
Markdown, then emails it via Gmail (smtplib + App Password).

## Environment setup

Always use a virtual environment for this project.

- venv location: `venv/` inside the project root
- Activate (Windows): `venv\Scripts\activate`
- Install dependencies into the venv, never globally
- Keep `requirements.txt` up to date after any new package is installed

Required packages:
- anthropic
- requests
- beautifulsoup4
- python-dotenv
- jinja2

Never use `pip install` without the venv being active.

## Model
Always use `claude-haiku-4-5-20251001` for all API calls. Never use Sonnet or Opus —
cost constraint. Haiku is ~5x cheaper than Sonnet for this structured generation task.

## Email config
- SMTP: smtp.gmail.com, port 587
- All credentials and addresses stored in `.env` — never hardcode them
- Required `.env` keys: `ANTHROPIC_API_KEY`, `GMAIL_APP_PASSWORD`, `MAIL_FROM`, `MAIL_TO`

## Commands

```bash
# Set up environment (first time)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run the digest
python digest.py

# Install a new package (venv must be active)
pip install <package>
pip freeze > requirements.txt
```

## Scheduling
Claude Code remote trigger — runs daily at 09:00 Europe/Helsinki (06:00 UTC).
Trigger ID: `trig_01H3NViVVFhGYrTXS4VyNu35`
Manage at: https://claude.ai/code/scheduled

## Architecture

`digest.py` is the single entry point with four stages:

**1. Load seen topics (`load_seen_topics`)**
Reads `seen_topics.json` from the project root. Prunes entries older than 7 days
in-memory. Returns a list of `{date, title, summary, source_urls}` dicts. Returns
`[]` if the file is missing or malformed — never crashes on a fresh install.

**1.5. Fetch & extract (`gather_context`)**
Uses `requests` + `BeautifulSoup` to fetch these sources directly:
- Hacker News front page — top 30 story titles + URLs
- GitHub Trending — repo name, URL, description
- HuggingFace Blog, OpenAI News, Anthropic News, GitHub Blog — titles + URLs via generic `<h2>`/`<h3>` extractor

Only title, URL, and a 1–2 sentence description are kept per item. Full article
body and HTML are discarded. Total context is hard-capped at 12,000 characters.

> **Why self-fetch instead of using Anthropic's web_search tool:**
> The server-side web_search tool passes raw fetched content directly into the
> Claude context, which pushed input token costs over $0.50/run. Self-fetching
> and extracting only headlines gives us full control over what enters the prompt.

**2. Generate digest (`generate_digest`)**
Single Claude API call — no agentic loop, no tools. The curated headline context
is embedded in the user message, preceded by the seen-topics block (see stage 1.5).
`SYSTEM_PROMPT` contains writing instructions: story selection criteria, voice/tone
rules, deduplication rules, and output delimiters. Claude does NOT generate HTML — only content.

Claude outputs only a structured JSON block, wrapped in:
```
<!-- BEGIN_JSON -->..<!-- END_JSON -->
```

The JSON schema has: `teaser`, `todays_pick`, `fun_fact`, and a `stories` array. Each story
has `title`, `category`, `is_lead`, `what_happened`, `why_it_matters`,
`action_type` (TRY IT / THE TAKE), `action_is_code`, `action_content`,
`source_name`, `source_url`.

`fun_fact` is a top-level one-liner — a punchy tech joke, surprising dev stat, or
absurd-but-true fact. Max 20 words, witty, no hashtags.

**3. Render Markdown (`render_markdown`)**
Python derives the `.md` file deterministically from the JSON using `render_markdown()`.
Claude no longer generates Markdown — this halves output tokens.

**4. Render HTML (`render_html`)**
Python renders `template.html` (Jinja2) with the parsed JSON. All visual styling
lives in `template.html` — update styles there, not in the prompt. A Jinja2
filter `md_links` converts `[text](url)` markdown links in story text to HTML
anchors.

The template uses an editorial "broadsheet" layout with Google Fonts (Newsreader
serif + IBM Plex Sans + IBM Plex Mono). CSS variables define the forest-green
palette; all layout is CSS grid/flexbox.

Template sections (top to bottom):
- **Masthead** — dark green (`#1B4332`) full-width bar; inline SVG two-square logo (greens `#2D6A4F` / `#74C69D`) + `TECH DIGEST` monospace wordmark + date; same SVG used as inline data-URI favicon
- **Hero** — cream background; large Newsreader serif teaser as H1; 2/3 + 1/3 grid:
  - *Lead story* (left): category kicker, title, `what_happened` in serif body, "Why it matters" left-border callout, action block (code or prose), source row
  - *Editor's Pick card* (right, sticky): dark green card with `todays_pick`, plus "At a Glance" category bar chart (CSS divs, no SVG)
- **Stories grid** — warm paper background; non-lead stories in a 3-column CSS grid; each card has category, title, body, action box, source
- **Fun Fact** — dark ink (`#14201B`) full-width strip; italic serif quote
- **Footer** — warm paper, monospace tagline

Stories are split in Jinja2: the `is_lead` story goes into the hero, all others into the grid.
Max-width is 1240px. Responsive breakpoint at `≤800px` collapses grid to single column.

**5. Save files (`save_files`)**
Writes to `digests/tech-digest-{YYYY-MM-DD}.md` and `.html`.
Also saves `digests/raw_response.txt` on every run — useful for debugging
if the delimiter parsing fails.

**6. Update seen topics (`save_seen_topics`)**
Called after `save_files` succeeds — never on error paths. Extracts the first
sentence of each story's `what_happened` as a summary, merges with prior entries,
re-prunes to 7 days, and writes `seen_topics.json`. The file accumulates at most
~35 entries (5 stories × 7 days).

**7. Send email (`send_email`)**
smtplib/STARTTLS. HTML file as email body, `.md` file as plain text attachment.
Subject: `Daily Tech Digest — {Full date}`.

## Topic deduplication

`seen_topics.json` in the project root is a JSON array of covered stories. It is:
- Auto-created on first successful run
- Pruned to a 7-day rolling window on every run
- Passed to Claude as context so it can skip exact repeats or flag follow-ups
- **Do not commit** this file (add to `.gitignore` if not already present)

Deduplication rules (enforced via `SYSTEM_PROMPT`):
- Skip a topic only if it is the exact same story with no meaningful new development
- Follow-ups (new release, major update, reversal, significant new data) are always covered
- When revisiting, Claude prefixes `what_happened` with "Previously covered on {date}: ..."
