# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Tech Digest — Project Instructions

## What this project does
Generates a daily tech news digest for **non-technical professionals** (teachers,
marketers, lawyers, designers, managers) and saves it as HTML and Markdown files
to `digests/`. The audience is smart and busy — they follow AI news because it
affects their work, not because they love technology.

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

## Environment variables
- Required `.env` key: `ANTHROPIC_API_KEY`

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

`digest.py` is the single entry point with six stages:

**1. Load seen topics (`load_seen_topics`)**
Reads `seen_topics.json` from the project root. Prunes entries older than 7 days
in-memory. Returns a list of `{date, title, summary, source_urls}` dicts. Returns
`[]` if the file is missing or malformed — never crashes on a fresh install.

**1.5. Fetch & extract (`gather_context`)**
Uses `requests` + `BeautifulSoup` to fetch these sources directly:
- Hacker News front page — top 30 story titles + URLs
- GitHub Trending — repo name, URL, description (up to 250 chars)
- HuggingFace Blog, Anthropic News, GitHub Blog — titles + URLs via generic `<h2>`/`<h3>` extractor (description up to 250 chars)

> OpenAI News is excluded — it reliably returns 403. OpenAI stories are well-covered via Hacker News.

After extraction, the top 3 articles from each blog source (HuggingFace, Anthropic,
GitHub Blog) are **enriched** via `enrich_items()`:
- `fetch_article_detail(url)` fetches each article page (timeout 8s) and extracts
  the `og:image` / `twitter:image` URL and the first substantial paragraph (≥80 chars, capped at 300 chars).
- Fetches run in parallel via `ThreadPoolExecutor(max_workers=8)`.
- URL validation in `fetch_article_detail` skips non-http(s) and private/loopback IPs
  to prevent SSRF. HN and GitHub Trending are never enriched: HN links arbitrary
  external sites (prompt injection risk), Trending links repo pages (no article content).

`format_section()` includes `description`, `Body:`, and `Image:` fields when present.
Total context hard-capped at 16,000 characters. The full context string is written to
`digests/raw_context.txt` after each run for debugging.

> **Why self-fetch instead of using Anthropic's web_search tool:**
> The server-side web_search tool passes raw fetched content directly into the
> Claude context, which pushed input token costs over $0.50/run. Self-fetching
> and extracting only headlines + article metadata gives us full control over what
> enters the prompt.

**2. Generate digest (`generate_digest`)**
Single Claude API call — no agentic loop, no tools. The curated headline context
is embedded in the user message, preceded by the seen-topics block. `SYSTEM_PROMPT`
targets a non-technical professional audience with a calm, clear journalistic voice.
Claude does NOT generate HTML or Markdown — only structured JSON.

Claude outputs only a structured JSON block, wrapped in:
```
<!-- BEGIN_JSON -->...<!-- END_JSON -->
```

The JSON schema:
```json
{
  "teaser": "One sentence for a non-technical reader.",
  "fun_fact": "Punchy one-liner or null. Max 20 words.",
  "lead_story": {
    "title": "...",
    "what_happened": "1–2 sentences, plain language.",
    "what_this_means": "1–2 sentences, professional audience relevance.",
    "visual_type": "image | chart | table | null",
    "visual_url": "https://... or null",
    "visual_data": { "headers": [...], "rows": [[...]] },
    "source_name": "...",
    "source_url": "https://..."
  },
  "quick_hits": [
    {
      "title": "...",
      "summary": "2–3 sentences, no jargon.",
      "visual_type": "...",
      "visual_url": "...",
      "visual_data": null,
      "source_name": "...",
      "source_url": "..."
    }
  ],
  "under_the_hood": [
    {
      "title": "...",
      "what_happened": "More technical detail than quick hits.",
      "why_it_matters": "Technical significance.",
      "code_example": "plain text, max 10 lines, or null",
      "visual_type": "...",
      "visual_url": null,
      "visual_data": null,
      "source_name": "...",
      "source_url": "..."
    }
  ]
}
```

- `quick_hits`: 3–4 items; `under_the_hood`: 1–2 items
- `visual_type`: exactly `"image"`, `"chart"`, `"table"`, or `null`
- `visual_url`: only URLs from provided source material — Claude must never fabricate
- `visual_data`: `{"headers": [...], "rows": [[...]]}` — populated only when numeric
  data or image URLs were present in the enriched context

**3. Render Markdown (`render_markdown`)**
Python derives the `.md` file deterministically from the JSON:
- Header + teaser
- Lead story: title, what_happened, what_this_means, source
- Quick Hits section: title + summary + source per story
- Under the Hood section: title + what_happened + why_it_matters + optional
  code_example block + source
- Fun fact at the bottom

**4. Render HTML (`render_html`)**
Python renders `template.html` (Jinja2) with the parsed JSON. All visual styling
lives in `template.html`. Custom Jinja2 filters:
- `md_links`: converts `[text](url)` markdown links to HTML anchors
- `chart_bars`: converts `visual_data` to `{label, value, pct}` dicts for CSS bar chart rendering

The template uses an editorial layout with Google Fonts (Newsreader serif + IBM Plex
Sans + IBM Plex Mono). CSS variables define the forest-green palette; all layout is
CSS grid/flexbox.

Template sections (top to bottom):
- **Masthead** — dark green (`#1B4332`) full-width bar; inline SVG two-square logo
  (greens `#2D6A4F` / `#74C69D`) + `TECH DIGEST` monospace wordmark + date
- **Hero** — cream background; large Newsreader serif teaser as H1; 2/3 + 1/3 grid:
  - *Lead story* (left): title, `what_happened`, optional visual, "What this means"
    left-border callout, source row
  - *Quick Hits sidebar* (right, sticky): dark green card listing quick hit titles as a preview
- **Quick Hits section** — warm paper background; 3-column CSS grid; cards alternate
  dark green (`#1B4332`) / light green (`#74C69D`) / dark green using `loop.index % 2`.
  Each card: title, `summary`, optional visual, source
- **Under the Hood section** — cream background; 2-column grid; each article: title,
  `what_happened`, "Why it matters" left-border callout, optional `code_example` pre
  block (dark terminal style), optional visual, source
- **Fun Fact** — dark ink (`#14201B`) full-width strip; italic serif quote
- **Footer** — warm paper, monospace tagline

Visual rendering (same pattern in all three sections):
- `visual_type == "image"`: `<img src="visual_url">`
- `visual_type == "chart"`: CSS bar rows via `chart_bars` filter
- `visual_type == "table"`: `<table>` with headers + rows from `visual_data`
- `null`: nothing rendered

Max-width 1240px. Responsive breakpoint at `≤800px` collapses to single column.

**5. Save files (`save_files`)**
Writes to `digests/tech-digest-{YYYY-MM-DD}.md` and `.html`.
Also saves on every run (overwritten each time):
- `digests/raw_response.txt` — Claude's raw output (debug delimiter parsing failures)
- `digests/raw_context.txt` — full context string sent to Claude (debug enrichment / missing visuals)

**6. Update seen topics (`save_seen_topics`)**
Called after `save_files` succeeds — never on error paths. `extract_seen_entries(data, date_str)`
collects entries from all three sections: lead_story and under_the_hood use `what_happened`,
quick_hits uses `summary`. Extracts the first sentence as a summary, merges with prior
entries, re-prunes to 7 days, and writes `seen_topics.json`. Accumulates at most ~42
entries (6–7 stories × 7 days).

## Topic deduplication

`seen_topics.json` in the project root is a JSON array of covered stories. It is:
- Auto-created on first successful run
- Pruned to a 7-day rolling window on every run
- Passed to Claude as context so it can skip exact repeats or flag follow-ups
- **Must be committed** to the repo — tracked in git so each run on a fresh checkout has topic history

Deduplication rules (enforced via `SYSTEM_PROMPT`):
- Skip a topic only if it is the exact same story with no meaningful new development
- Follow-ups (new release, major update, reversal, significant new data) are always covered
- When revisiting, Claude prefixes `what_happened` with "Previously covered on {date}: ..."
