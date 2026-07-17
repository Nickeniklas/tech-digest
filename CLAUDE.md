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
Default is `claude-haiku-4-5-20251001` for all API calls. Never use Sonnet or Opus by
default — cost constraint. Haiku is ~5x cheaper than Sonnet for this structured
generation task. The default can be overridden via `DIGEST_MODEL` (see below) for
self-hosting/testing, but don't change the default in code without being asked.

## Environment variables
- Required `.env` key: `ANTHROPIC_API_KEY`
- Optional `.env` key: `DIGEST_MODEL` — overrides the model id, default `claude-haiku-4-5-20251001`
- Optional `.env` key: `DIGEST_BASE_URL` — if set, passed as `base_url=` to `anthropic.Anthropic(...)`,
  for pointing at a LiteLLM proxy or self-hosted Anthropic-compatible endpoint

## Commands

```bash
# Set up environment (first time)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run the digest (full local run: gather -> Claude API -> finish)
python digest.py

# Or run the two stages separately (no API call needed to test rendering —
# see "Testing digest.py's CLI stages" below)
python digest.py gather
python digest.py finish build/digest_raw.txt

# Install a new package (venv must be active)
pip install <package>
pip freeze > requirements.txt
```

### Testing template/HTML changes without an API call

`python digest.py` skips generation if `digests/tech-digest-{today}.html` already
exists, and a real run costs a (small) API call. To preview `template.html` edits
against today's real content for free, re-render from the saved raw response:

```python
from digest import parse_output, render_html
from pathlib import Path
data = parse_output(Path("digests/raw_response.txt").read_text(encoding="utf-8"))
html = render_html(data, "Thursday, June 11 2026")  # full_date string
Path("digests/tech-digest-2026-06-11.html").write_text(html, encoding="utf-8")
```
Then open the `.html` file directly in a browser.

### Regenerating archive.html without an API call

If `archive.html` goes stale (e.g. a run committed a digest but not the archive),
rebuild it from the existing `digests/` folder — no API call, no new digest:
```python
from digest import build_archive_entries, render_archive
from pathlib import Path
Path("archive.html").write_text(render_archive(build_archive_entries()), encoding="utf-8")
```

### Testing digest.py's CLI stages without an API call

`python digest.py gather` and `python digest.py finish <path>` can be exercised
independently, at zero API cost:

- `gather` only skips (`SKIP`) if today's `digests/tech-digest-{date}.html`
  already exists — otherwise it does a real (free) fetch of all five sources
  and writes `build/gather_output.txt` + `build/known_urls.txt`.
- `finish` needs a raw JSON response file (delimited by `<!-- BEGIN_JSON -->` /
  `<!-- END_JSON -->`) and `build/known_urls.txt` to already exist. Write a
  small synthetic JSON matching the schema (see the schema below), or reuse
  `digests/raw_response.txt` from a prior real run.

If today's real digest already exists and you need `gather` to actually run
(not `SKIP`), temporarily move `digests/tech-digest-{date}.md`/`.html` (and
`archive.html`, `index.html`, `seen_topics.json` if you're also testing
`finish`) aside first — `finish` overwrites all of these. Since they're
git-tracked, `git checkout -- <paths>` restores the real committed content
afterward; `build/` is gitignored so it's safe to delete once done.

### Testing digest.py logic with no dependencies installed

`import digest` fails without `anthropic`/`requests`/`bs4`/`dotenv` installed, even
when testing logic that needs none of them. Stub them first:
```python
import sys, types
for name in ("anthropic", "requests", "bs4", "dotenv"):
    sys.modules[name] = types.ModuleType(name)
sys.modules["anthropic"].Anthropic = object
sys.modules["requests"].exceptions = types.SimpleNamespace(
    HTTPError=type("HTTPError", (Exception,), {})
)
sys.modules["bs4"].BeautifulSoup = object
sys.modules["dotenv"].load_dotenv = lambda *a, **k: None
```
The `requests.exceptions` line is only needed if the code under test *calls*
`fetch_page` (its `except requests.exceptions.HTTPError` clause resolves at raise
time, not import time). Without it you get `module 'requests' has no attribute
'exceptions'` rather than the real failure. Import and the pure-logic functions
work without it.

### Tests

`tests/test_sanitize.py` covers `sanitize_story_urls`: untrusted URLs dropped,
known URLs kept, and malformed model output (`lead_story: None`, a null section,
a bare string where a story dict belongs) not raising. It uses the stub recipe
above, so it needs no venv and no installed dependencies:

```bash
python tests/test_sanitize.py    # prints PASS/FAIL per test, exit 1 on failure
```

No pytest — plain asserts and a `__main__` runner, deliberately, so the routine
environment can run it without installing anything.

## Scheduling
Claude Code remote trigger — runs daily at 06:45 Europe/Helsinki (03:45 UTC).
Trigger ID: `trig_01H3NViVVFhGYrTXS4VyNu35`
Manage at: https://claude.ai/code/routines

**The scheduled run's entire prompt is just "open `ROUTINE.md` and follow it."**
As of the July 2026 pipeline-unification pass, all pipeline logic lives in
`digest.py` — the trigger config no longer contains any inline `python -c`
pipeline steps. `ROUTINE.md` calls `python digest.py gather`, has the routine
agent generate the digest JSON itself (reading `prompts/system_prompt.md` as
its system prompt — the same file the local API path loads), then
`python digest.py finish build/digest_raw.txt`, then commits and pushes.

Because both the local (`python digest.py`) and routine paths call the same
`gather_stage()` / `finish_stage()` functions, there is nothing left to keep in
sync by hand — any `digest.py` signature or pipeline change is automatically
picked up by both paths. Only edit the trigger itself (via the `RemoteTrigger`
tool) if the schedule, model, or top-level instructions change; day-to-day
pipeline changes only need `digest.py` and `ROUTINE.md` edited.

## Architecture

`digest.py` is the single entry point, structured as two composable pipeline
stages plus a thin CLI:

- `gather_stage()` — load seen topics + `gather_context()`. Returns `None` if
  today's digest already exists (nothing to do), otherwise a dict with
  `date_str`, `full_date`, `seen_topics`, `seen_block`, `image_refs`, `context`,
  `known_urls`.
- `finish_stage(date_str, full_date, raw, known_urls)` — `parse_output` →
  `sanitize_story_urls` → `render_markdown` → `render_html` → `save_files` →
  `extract_seen_entries` + `save_seen_topics` → regenerate `archive.html` →
  `update_index_html`.

Three ways to invoke them:
- `python digest.py` (no args) — `main()`, composed as gather_stage → call the
  Anthropic API (`generate_digest`, stage 2 below) → finish_stage. Full local run.
- `python digest.py gather` — runs `gather_stage()` only. Prints `SKIP` and exits
  if today's digest exists; otherwise writes `build/gather_output.txt` (labeled
  `IMAGE_REFS` / `SEEN_BLOCK` / `CONTEXT` sections) and `build/known_urls.txt`,
  then prints `PROCEED:{date_str}`. This is what `ROUTINE.md` calls so the
  scheduled agent (which IS the AI — no API call) can read the same context a
  local run would send to Claude.
- `python digest.py finish <raw_response_path>` — runs `finish_stage()` against
  an already-generated raw response file, reading `known_urls` back from
  `build/known_urls.txt`. Also what `ROUTINE.md` calls, after the routine agent
  writes its own generated JSON to `build/digest_raw.txt`.

`build/` is gitignored — everything in it is regenerated every run, same as
`digests/raw_response.txt` and `digests/raw_context.txt`.

Since both the local API path and the scheduled routine call these same two
functions, there is exactly one implementation of each pipeline stage — nothing
to keep in sync by hand across two code paths anymore.

The six logical stages below are unchanged in behavior from before the CLI
refactor — only how they're invoked (directly in `main()` vs. via the `gather`/
`finish` subcommands) changed:

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

> Anthropic News must be fetched as `https://www.anthropic.com/news`, **with** the
> `www`. The bare `anthropic.com` redirects, and the routine environment's proxy
> denies the redirect hop — surfacing as a 403 that looks identical to a
> server-side block. The same `www` URL is passed as `extract_generic`'s
> `base_url`, since relative hrefs are joined onto it and would otherwise
> reintroduce the redirect on every enriched article fetch. `www.anthropic.com`
> is on the routine environment's allowlist (added July 2026).

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

`gather_context()` returns a **tuple** `(context_str, image_refs_block, known_urls)`.
`known_urls` is every URL actually fetched — used after generation to validate
Claude's output (see stage 2.5 below). The
`image_refs_block` is a compact string listing every `image_url` found across all
enriched items, keyed to article title:
```
Available image URLs (use these verbatim for matching stories — do not use any other URLs):
  - "Article title": https://...
```
This block is prepended to the Claude user message before the headlines so Claude
can easily match image URLs to the stories it selects, rather than hunting through
the full 16k-char context.

> **Why self-fetch instead of using Anthropic's web_search tool:**
> The server-side web_search tool passes raw fetched content directly into the
> Claude context, which pushed input token costs over $0.50/run. Self-fetching
> and extracting only headlines + article metadata gives us full control over what
> enters the prompt.

**2. Generate digest (`generate_digest`)**
Single Claude API call — no agentic loop, no tools. The user message is assembled in
this order:
1. Today's date
2. `image_refs_block` (if any image URLs were found — see step 1.5)
3. Seen-topics block (if any)
4. Full headline context

`SYSTEM_PROMPT` is loaded at import time from `prompts/system_prompt.md`
(`SYSTEM_PROMPT = (Path(__file__).parent / "prompts" / "system_prompt.md").read_text(...).strip()`)
— that file is the single source of truth for the editorial brief, read by both
the local API path and the routine agent (via `ROUTINE.md`, which tells it to
read that file directly and follow it as its own system prompt). Never edit the
brief as an inline string in `digest.py` again. It targets a non-technical
professional audience with a calm, clear journalistic voice. Claude does NOT
generate HTML or Markdown — only structured JSON.

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
- `visual_url`: ONLY a URL from the `image_refs_block` — never constructed or guessed; if no matching URL exists, use `null` and fall back to `"chart"` or `"table"`
- `visual_data`: Claude-synthesized from numbers, benchmarks, or comparisons in the story text — do not leave `null` when quantitative data exists; format `{"headers": [...], "rows": [[...]]}`
- The prompt mandates **at least 2 visuals** across the full digest; lead_story always attempts one

**2.5. Sanitize URLs (`sanitize_story_urls`)**
Called in `finish_stage()` right after `parse_output`. Drops any `source_url`/`visual_url`
not in `known_urls` — the real enforcement, since the prompt instruction alone
isn't a safety boundary against scraped content designed to override it.

Model output is untrusted JSON, so both this and `extract_seen_entries` treat the
schema as advisory: a missing or `null` `lead_story`, a `null` section, and
non-dict entries inside a section are all skipped rather than raised on. Note
`data.get("quick_hits", [])` is *not* sufficient — a key present with a `null`
value returns `None`, not the default, and blows up the `*` unpack. Use
`data.get("quick_hits") or []`.

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
- `md_links`: converts `[text](url)` markdown links to HTML anchors (with `target="_blank" rel="noopener"`)
- `chart_bars`: converts `visual_data` to `{label, value, pct}` dicts for CSS bar chart rendering

Both Jinja `Environment`s (`render_html`, `render_archive`) use `autoescape=True`.
`_md_links_to_html` is the only filter rendered with `| safe` — it does its own
escaping and only allows `http(s)://` links through. Don't add `| safe` elsewhere.

All outbound source links (lead story, quick hits, under the hood) and inline
`md_links` anchors open in a new tab via `target="_blank" rel="noopener"`, so
readers never navigate away from the digest itself.

The template uses an editorial layout with Google Fonts (Newsreader serif + IBM Plex
Sans + IBM Plex Mono). CSS variables define the forest-green palette; all layout is
CSS grid/flexbox.

Template sections (top to bottom):
- **Masthead** — dark green (`#1B4332`) full-width bar; inline SVG two-square logo
  (greens `#2D6A4F` / `#74C69D`) + `TECH DIGEST` monospace wordmark + date
- **Hero** — cream background; large Newsreader serif teaser as H1; 2/3 + 1/3 grid:
  - *Lead story* (left): title, `what_happened`, optional visual, "What this means"
    left-border callout, source row
  - *Quick Hits sidebar* (right, sticky): dark green card listing quick hit titles as a
    preview; each title is a link (`#qh-item-N`) to the matching accordion item below
- **Quick Hits section** — warm paper background; vertical accordion using native
  `<details>`/`<summary>` elements. Each item collapses to title +
  source pill (green pill, `#74C69D` background); expanding reveals `summary`, optional
  visual, and source link. Chevron rotates 90° on open via `details[open]` CSS selector.
  Each `<details id="qh-item-N">` matches a sidebar link. A small inline `<script>`
  (end of `<body>`) sets `details.open = true` on click and on initial hash navigation
  so the browser scrolls to an already-expanded item; `.qh-item` has
  `scroll-margin-top` so the expanded item isn't flush against the viewport edge.
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
Also saved (overwritten each time):
- `digests/raw_response.txt` — Claude's raw output, written by `parse_output()`
  inside `finish_stage()` (debug delimiter parsing failures) — every path
- `digests/raw_context.txt` — full context string sent to Claude (debug
  enrichment / missing visuals) — only `python digest.py` (full local run)
  writes this; `python digest.py gather` writes the equivalent context to
  `build/gather_output.txt` instead

**6. Update seen topics (`save_seen_topics`)**
Called in `finish_stage()` after `save_files` succeeds — never on error paths.
`extract_seen_entries(data, date_str)` collects entries from all three sections:
lead_story and under_the_hood use `what_happened`, quick_hits uses `summary`.
Extracts the first sentence as a summary, merges with prior entries, re-prunes
to 7 days, and writes `seen_topics.json`. Accumulates at most ~42 entries
(6–7 stories × 7 days).

`source_urls` must be `[]`, never `[None]`, when the story has no `source_url`.
This matters across days, not just within a run: `extract_seen_entries` runs
*after* `sanitize_story_urls` may have nulled a URL, and the next day's
`format_seen_topics_context` does `", ".join(e["source_urls"])` — a `[None]`
written today raises `TypeError` on tomorrow's run. Fixed July 2026; entries
written before then age out of the 7-day window on their own.

**7. Regenerate archive and index (`build_archive_entries`, `render_archive`, `update_index_html`)**
Runs at the end of every `finish_stage()` call — i.e. both the local and routine
paths, since both call `finish_stage()`. Rewrites `archive.html` (via
`archive_template.html`) listing every past digest, and rewrites `index.html` to
meta-refresh to today's digest. `index.html` regeneration used to live only in
the routine's inline Step 6, so local-only runs left the redirect stale — as of
the CLI refactor it's part of the shared stage and both paths update it. Not
linked from `index.html` — v0.1, reachable only by typing `/archive.html`
directly.

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
