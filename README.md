# tech-digest

Daily tech news digest for busy professionals. Fetches the latest AI and dev tools news from high-signal sources, summarizes it with Claude for a non-technical audience, and saves a styled HTML page and Markdown file to `digests/`.

## What it does

1. Fetches HackerNews, GitHub Trending, HuggingFace Blog, Anthropic News, and GitHub Blog for today's most relevant AI and tech news
2. Enriches the top 3 articles from each blog source by fetching their pages for og:image URLs and opening paragraphs — giving Claude richer material for visuals and summaries
3. Generates a digest in three sections: a **Lead Story**, 3–4 **Quick Hits**, and 1–2 **Under the Hood** deep dives
4. Renders a polished HTML page and a Markdown file, both saved to `digests/`
5. Updates a rolling 7-day topic index so stories aren't repeated

The HTML uses an editorial layout: a serif teaser, a hero section with the lead story and a sticky **Quick Hits** sidebar preview, a **Quick Hits accordion** (each item collapses to title + source pill; click to expand full summary and any visual — built on native `<details>`/`<summary>`), a 2-column **Under the Hood** section with optional code blocks and data visuals (images, CSS bar charts, tables), and a **Fun Fact** strip. Typeset in Newsreader + IBM Plex. Max-width 1240px, responsive at 800px.

Clicking a title in the Quick Hits sidebar jumps to and expands the matching accordion
item below (a small inline script). All outbound source links open in a new tab.

The site's root URL (`index.html`) always serves today's digest directly — not a
redirect — so it's installable via iOS/Android "Add to Home Screen" as a
standalone, app-like bookmark (via `manifest.json`) that stays current day to day.

## Requirements

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com) (uses `claude-haiku-4-5-20251001`)

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

Optionally, set `DIGEST_MODEL` to override the default model (`claude-haiku-4-5-20251001`)
and `DIGEST_BASE_URL` to point the Anthropic client at a self-hosted endpoint — e.g. a
LiteLLM proxy or any Anthropic-compatible server — instead of the public Anthropic API.

## Usage

```bash
python digest.py
```

`digest.py` also exposes the pipeline as two CLI subcommands, used by `ROUTINE.md` (see
Scheduling below) and useful for debugging without an API call:

```bash
python digest.py gather                    # fetch headlines -> build/gather_output.txt
python digest.py finish build/digest_raw.txt  # render + save from a raw JSON response
```

## Tests

```bash
python tests/test_sanitize.py
```

Covers URL sanitization and tolerance of malformed model output. Stubs its
third-party imports, so it runs on a bare interpreter — no venv, no pytest, no
API key.

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

Runs daily at 06:45 Europe/Helsinki (03:45 UTC) via a scheduled remote Claude Code agent.
The trigger's entire prompt is "open `ROUTINE.md` and follow it" — all pipeline logic
lives in `digest.py`, not in the trigger config. The flow, per `ROUTINE.md`:

1. Set up the Python environment (`venv` + `pip install -r requirements.txt`)
2. Run `python digest.py gather` to fetch headlines (stops if `SKIP` — today's digest exists)
3. The agent itself generates the digest JSON, reading `prompts/system_prompt.md` as its
   system prompt — no separate Anthropic API call; the remote agent IS the AI
4. Run `python digest.py finish build/digest_raw.txt` to render HTML/Markdown, save files,
   and regenerate `archive.html` and `index.html`
5. Commit `digests/`, `index.html`, `seen_topics.json`, `archive.html` and push to the
   routine's checked-out branch. A GitHub Actions workflow
   (`.github/workflows/auto-merge-claude.yml`) merges `main` into that branch (resolving
   conflicts in favour of the new digest), opens a PR, squash-merges into `main`, then
   deletes the branch

Manage the routine at https://claude.ai/code/routines.

Both the routine and a local `python digest.py` run call the same `gather_stage()` /
`finish_stage()` functions in `digest.py`, so there's a single implementation of the
pipeline shared by both paths — nothing to keep in sync by hand.

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
├── digest.py           # Main script — gather_stage()/finish_stage() + CLI (gather/finish/full run)
├── ROUTINE.md          # Complete instructions for the scheduled remote agent
├── prompts/
│   └── system_prompt.md  # Editorial brief — single source of truth, read by both the
│                          # local API path and the routine agent
├── template.html       # Jinja2 HTML template
├── archive_template.html  # Jinja2 template for the archive listing
├── archive.html        # Listing of all past digests (regenerated every run)
├── index.html          # Today's digest, served at the root (regenerated by both local and routine runs)
├── manifest.json       # PWA manifest, for iOS/Android "Add to Home Screen"
├── seen_topics.json    # Rolling 7-day topic index (committed; gives each run topic memory)
├── assets/
│   ├── favicon.svg           # Site favicon (two-square logo, forest-green palette)
│   ├── apple-touch-icon.png  # 180x180, for iOS "Add to Home Screen"
│   ├── icon-192.png          # PWA manifest icon
│   └── icon-512.png          # PWA manifest icon
├── tests/
│   └── test_sanitize.py  # Dependency-free tests — python tests/test_sanitize.py
├── docs/               # Backlog and project-context notes
├── CLAUDE.md           # Claude Code instructions
├── requirements.txt
├── .env                # API keys (never commit this)
├── .gitignore
├── build/              # Intermediate pipeline files (gitignored, regenerated every run)
└── digests/            # Generated output files
```
