# tech-digest

Daily tech news digest for busy professionals. Fetches the latest AI and dev tools news from high-signal sources, summarizes it with Claude for a non-technical audience, and saves a styled HTML page and Markdown file to `digests/`.

## What it does

1. Fetches HackerNews, GitHub Trending, HuggingFace Blog, Anthropic News, and GitHub Blog for today's most relevant AI and tech news
2. Enriches the top 3 articles from each blog source by fetching their pages for og:image URLs and opening paragraphs — giving Claude richer material for visuals and summaries
3. Generates a digest in three sections: a **Lead Story**, 3–4 **Quick Hits**, and 1–2 **Under the Hood** deep dives
4. Renders a polished HTML page and a Markdown file, both saved to `digests/`
5. Updates a rolling 7-day topic index so stories aren't repeated

The HTML uses an editorial layout: a serif teaser, a hero section with the lead story and a sticky **Quick Hits** preview card, a 3-column **Quick Hits** grid (alternating dark/light green cards), a 2-column **Under the Hood** section with optional code blocks and data visuals (images, CSS bar charts, tables), and a **Fun Fact** strip. Typeset in Newsreader + IBM Plex. Max-width 1240px, responsive at 800px.

## Requirements

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com) (uses `claude-haiku-4-5`)

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
```

## Usage

```bash
python digest.py
```

Output files are saved to `digests/`, and a topic index is maintained in the project root:

```
digests/
├── tech-digest-2026-04-26.md
├── tech-digest-2026-04-26.html
├── raw_response.txt     # Claude's raw JSON output — debug delimiter parsing
└── raw_context.txt      # Full context sent to Claude — debug enrichment / missing visuals
seen_topics.json         # Rolling 7-day index of covered topics (committed to git)
```

## Scheduling

Runs daily at 09:00 Europe/Helsinki (06:00 UTC) via a Claude Code remote trigger. The flow:

1. CCR creates a `claude/YYYYMMDD` branch and runs `digest.py`
2. Generated files (`digests/`, `seen_topics.json`) are committed and pushed
3. A GitHub Actions workflow (`.github/workflows/auto-merge-claude.yml`) opens a PR and squash-merges it into `main`, then deletes the branch

Manage the trigger at https://claude.ai/code/scheduled.

To run locally on demand:

```bash
python digest.py
```

## Cost

Roughly **$0.01–0.03 per run** using `claude-haiku-4-5-20251001`. At daily usage that's <$1/month.

This is achieved by: self-fetching headlines (no web_search tool), outputting JSON only (Markdown and HTML are derived in Python), a trimmed context cap of 16k chars, using Haiku instead of Sonnet, and a rolling 7-day topic index that keeps the seen-topics context small.

## Project structure

```
tech-digest/
├── digest.py          # Main script
├── template.html      # Jinja2 HTML template
├── index.html         # Redirects to latest digest (auto-updated by remote agent)
├── seen_topics.json   # Rolling 7-day topic index (committed; gives each run topic memory)
├── assets/
│   └── favicon.svg    # Site favicon (two-square logo, forest-green palette)
├── CLAUDE.md          # Claude Code instructions
├── FUTURE.md          # Backlog / ideas
├── requirements.txt
├── .env               # API keys (never commit this)
├── .gitignore
└── digests/           # Generated output files
```
