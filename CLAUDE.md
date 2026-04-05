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
Always use `claude-sonnet-4-6` for all API calls. Never use Opus —
cost constraint, not a quality decision.

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
Windows Task Scheduler — runs daily at 07:00

## Architecture

`digest.py` is the single entry point with four stages:

**1. Fetch & extract (`gather_context`)**
Uses `requests` + `BeautifulSoup` to fetch these sources directly:
- Hacker News front page — top 30 story titles + URLs
- GitHub Trending — repo name, URL, description
- HuggingFace Blog, OpenAI News, Anthropic News, GitHub Blog — titles + URLs via generic `<h2>`/`<h3>` extractor

Only title, URL, and a 1–2 sentence description are kept per item. Full article
body and HTML are discarded. Total context is hard-capped at 20,000 characters.

> **Why self-fetch instead of using Anthropic's web_search tool:**
> The server-side web_search tool passes raw fetched content directly into the
> Claude context, which pushed input token costs over $0.50/run. Self-fetching
> and extracting only headlines gives us full control over what enters the prompt.

**2. Generate digest (`generate_digest`)**
Single Claude API call — no agentic loop, no tools. The curated headline context
is embedded in the user message. `SYSTEM_PROMPT` contains writing instructions:
story selection criteria, voice/tone rules, accessibility guidance, and output
delimiters. Claude does NOT generate HTML — only content.

Claude outputs structured JSON + Markdown, wrapped in:
```
<!-- BEGIN_JSON -->..<!-- END_JSON -->
<!-- BEGIN_MARKDOWN -->..<!-- END_MARKDOWN -->
```

The JSON schema has: `teaser`, `todays_pick`, and a `stories` array. Each story
has `title`, `category`, `is_lead`, `what_happened`, `why_it_matters`,
`action_type` (TRY IT / THE TAKE), `action_is_code`, `action_content`,
`source_name`, `source_url`.

**3. Render HTML (`render_html`)**
Python renders `template.html` (Jinja2) with the parsed JSON. All email styling
lives in `template.html` — update styles there, not in the prompt. A Jinja2
filter `md_links` converts `[text](url)` markdown links in story text to HTML
anchors.

**4. Save files (`save_files`)**
Writes to `digests/tech-digest-{YYYY-MM-DD}.md` and `.html`.
Also saves `digests/raw_response.txt` on every run — useful for debugging
if the delimiter parsing fails.

**5. Send email (`send_email`)**
smtplib/STARTTLS. HTML file as email body, `.md` file as plain text attachment.
Subject: `Daily Tech Digest — {Full date}`.
