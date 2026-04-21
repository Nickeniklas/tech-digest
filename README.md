# tech-digest

Daily tech news digest for developers. Fetches the latest AI and dev tools news from high-signal sources, summarizes it with Claude, and emails a styled HTML newsletter to your inbox every morning.

## What it does

1. Fetches HackerNews, GitHub Trending, HuggingFace, OpenAI, Anthropic, and GitHub Blog for today's most relevant developer news
2. Selects the 3–5 most actionable stories and writes them up with an editorial voice
3. Generates a polished HTML email (green-on-white, responsive) and a Markdown file
4. Sends the email via Gmail and saves both files locally

The email includes a **Digest at a Glance** bar chart, full-width category section headers, a **Fun Fact** footer, and a **Today's Pick** editorial banner. Layout is optimised for desktop (680px) with a mobile fallback.

## Requirements

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com) (uses `claude-haiku-4-5`)
- A Gmail account with [App Password](https://myaccount.google.com/apppasswords) enabled (requires 2FA)

## Setup

```bash
git clone https://github.com/yourusername/tech-digest
cd tech-digest

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=sk-ant-...
GMAIL_APP_PASSWORD=your16charpassword
MAIL_FROM=you@gmail.com
MAIL_TO=you@gmail.com
```

## Usage

```bash
python digest.py
```

Output files are saved to `digests/`, and a topic index is maintained in the project root:

```
digests/
├── tech-digest-2026-04-02.md
├── tech-digest-2026-04-02.html
└── raw_response.txt        # Claude's raw output, useful for debugging
seen_topics.json            # Rolling 7-day index of covered topics (auto-managed)
```

## Scheduling

Runs daily at 09:00 Europe/Helsinki via a Claude Code remote trigger (CCR). The remote agent clones the repo, generates the digest, commits the output files, and pushes to `main`. Manage the trigger at https://claude.ai/code/scheduled.

To run locally on demand:

```bash
python digest.py
```

## Cost

Roughly **$0.01–0.03 per run** using `claude-haiku-4-5-20251001`. At daily usage that's <$1/month.

This is achieved by: self-fetching headlines (no web_search tool), outputting JSON only (Markdown is derived in Python), a trimmed context cap of 12k chars, using Haiku instead of Sonnet, and a rolling 7-day topic index that keeps the seen-topics context small (~2k tokens max).

## Project structure

```
tech-digest/
├── digest.py          # Main script
├── template.html      # Jinja2 email template
├── index.html         # Redirects to latest digest (auto-updated by remote agent)
├── seen_topics.json   # Rolling 7-day topic index (auto-created, do not commit)
├── CLAUDE.md          # Claude Code instructions
├── FUTURE.md          # Backlog / ideas
├── requirements.txt
├── .env               # API keys (never commit this)
├── .gitignore
└── digests/           # Generated output files
```