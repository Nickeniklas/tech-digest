# Tech Digest — Project Context

## What this project is
A daily automated tech news digest for **non-technical professionals** (teachers, marketers, lawyers, designers, managers). A pipeline fetches headlines from high-signal sources, has Claude write a structured digest, and renders it as styled HTML and Markdown. Live for several months. No email, no manual steps.

## Output
- `digests/tech-digest-{YYYY-MM-DD}.md` and `.html`
- `archive.html` (repo root) — listing of all past digests, regenerated every run
- `index.html` — redirect to the latest digest, regenerated every run (both paths)
- Debug artifacts, overwritten each run: `digests/raw_response.txt`, `digests/raw_context.txt`
- Intermediate files in gitignored `build/` (gather output, known URLs, routine raw response)

## Architecture — unified two-path design (July 2026 refactor, commit c652f60)
Both execution paths run the **same code** (`digest.py` stages) and read the **same editorial prompt** (`prompts/system_prompt.md`). The only difference is who writes the digest JSON.

**Path 1 — Local run:** `python digest.py` → full pipeline, digest JSON written by a Claude API call.
**Path 2 — Scheduled routine (06:45 Europe/Helsinki, trigger `trig_01H3NViVVFhGYrTXS4VyNu35`):** the trigger prompt is ~4 lines pointing at repo-tracked `ROUTINE.md`. The routine agent runs `python digest.py gather`, writes the digest JSON itself (no API call) following `prompts/system_prompt.md`, runs `python digest.py finish build/digest_raw.txt`, then commits and pushes. **No pipeline logic lives in the trigger config.**

### CLI subcommands
- `python digest.py` — full local run (gather → API generate → finish)
- `python digest.py gather` — dedupe check (prints `SKIP` if today's digest exists), fetch + enrich sources, write `build/gather_output.txt` (IMAGE_REFS / SEEN_BLOCK / CONTEXT sections) and `build/known_urls.txt`
- `python digest.py finish <raw_path>` — parse, sanitize URLs, render MD+HTML, save, update seen topics, regenerate `archive.html` and `index.html`

## Where the writing logic lives
All prose comes from a Claude model following `prompts/system_prompt.md` — the single source of truth: audience, calm journalistic voice (no hype), three-section structure, visual rules, dedup rules, exact JSON schema. `digest.py` loads it at import; the routine agent reads the same file. Python code composes zero sentences — it fetches, validates, and mechanically renders JSON.

## Digest structure
JSON wrapped in `<!-- BEGIN_JSON --> ... <!-- END_JSON -->`:
- `teaser` — one sentence for a non-technical reader
- `lead_story` — title, what_happened, what_this_means, visual fields, source
- `quick_hits` — 3–4 short stories, 2–3 sentences, no jargon
- `under_the_hood` — 1–2 technical stories, optional ≤10-line code example
- `fun_fact` — punchy one-liner or null
- Visuals per story: `visual_type` ("image"|"chart"|"table"|null), `visual_url` (verbatim from fetched context only), `visual_data` (synthesized headers/rows). ≥2 visuals mandated per digest.

## Pipeline stages
1. `load_seen_topics()` — `seen_topics.json`, pruned to 7-day window
2. `gather_context()` — scrapes Hacker News, GitHub Trending, HuggingFace Blog, Anthropic News, GitHub Blog (OpenAI blog excluded — reliable 403; HN covers it). Enriches top 3 blog articles with og:image + first paragraph (parallel, SSRF-guarded). **Fail-loud:** RuntimeError if <3 of 5 sources return content. Context capped at 16k chars. Returns `(context, image_refs, known_urls)`.
3. Generation — Haiku API call (local) or routine agent (scheduled), same prompt
4. `parse_output()` — extract JSON from delimiters
5. `sanitize_story_urls()` — drops any source_url/visual_url not in `known_urls`; the real security boundary against scraped-content prompt injection. Guards non-dict stories.
6. `render_markdown()` + `render_html()` — deterministic; Jinja2 `template.html`, autoescape on; only the self-escaping `md_links` filter uses `| safe`
7. Save files → update seen topics (only after successful save) → regenerate `archive.html` + `index.html`

Rerun-safe: skips if today's digest already exists.

## Model & self-hosting
- Default model: `claude-haiku-4-5-20251001` (cost rule — ~$0.01–0.03/run local)
- Env overrides: `DIGEST_MODEL`, `DIGEST_BASE_URL` (Anthropic client `base_url`) — enables LiteLLM proxy or Anthropic-compatible self-hosted endpoints
- `load_dotenv()` runs at module import so overrides apply before config is read
- Required env: `ANTHROPIC_API_KEY` (local path only)

## Automation details
- Routine commits directly per ROUTINE.md: `git add digests/ index.html seen_topics.json archive.html`, commit, push
- GitHub Actions workflow (`.github/workflows/auto-merge-claude.yml`) handles claude/ branch auto-merging
- Manage routine at https://claude.ai/code/routines

## Deduplication
`seen_topics.json` (repo root, **committed** — being gitignored previously caused daily repeats). Rolling 7-day window, ~42 entries max. Passed as context; exact repeats skipped, follow-ups prefixed "Previously covered on {date}: ...".

## Files
- `digest.py` — single entry point + CLI subcommands
- `prompts/system_prompt.md` — the editorial brief, single source of truth
- `ROUTINE.md` — full routine instructions (trigger config just points here)
- `template.html`, `archive_template.html` — Jinja2 templates (editorial layout, Newsreader + IBM Plex, forest-green palette, Quick Hits accordion)
- `index.html`, `assets/favicon.svg`
- `seen_topics.json` — committed dedup memory
- `tests/test_sanitize.py` — dependency-free tests for `sanitize_story_urls` (`python tests/test_sanitize.py`)
- `build/` — gitignored intermediates
- `CLAUDE.md`, README, FUTURE.md, `.github/workflows/auto-merge-claude.yml`, `requirements.txt`

## Constraints & principles
- **Fail loud** — abort with informative errors rather than emit a hollow digest
- **No logic outside the repo** — trigger config must never carry pipeline steps or prompts
- Self-fetch headlines instead of web_search tool (cost + context control)
- Windows dev environment, venv mandatory

## Status
- Unification refactor merged and pushed (c652f60); trigger updated to ROUTINE.md pointer. **First scheduled run on the new path landed successfully** — digest for 2026-07-17 committed via PR #45 (c1e9902). The two-path design is confirmed working end to end.
- Beginner-friendly rewrite: merged and live
- Routine-environment allowlist 403s: **Anthropic addressed July 2026** — the fetch URL is now `https://www.anthropic.com/news` (bare `anthropic.com` redirects; the proxy denied the hop) and `www.anthropic.com` was added to the environment allowlist. `fetch_page` now logs the status code and any `x-deny-reason` header on HTTPError, so a proxy denial is distinguishable from a server-side block instead of both reading as a bare 403. HuggingFace has not been re-checked — if it 403s, read the new warning to tell which kind it is. The <3-of-5 guardrail still catches total failure.
- Hardening (July 2026): `sanitize_story_urls` and `extract_seen_entries` tolerate malformed model JSON; `seen_topics.json` no longer written with `[None]` source_urls (which crashed the *following* day's run). Covered by `tests/test_sanitize.py`.

## Backlog (FUTURE.md)
Archive page polish, PWA support, push notifications, search across digests, mobile styling improvements.
