# Tech Digest — Project Context

## What this project is
A daily automated tech news digest for **non-technical professionals** (teachers, marketers, lawyers, designers, managers). A pipeline fetches headlines from high-signal sources, has Claude write a structured digest, and renders it as styled HTML and Markdown. Live for several months. No email, no manual steps.

## Output
- `digests/tech-digest-{YYYY-MM-DD}.md` and `.html`
- `archive.html` (repo root) — listing of all past digests, regenerated every run
- `index.html` — redirects to the latest digest
- Debug artifacts, overwritten each run: `digests/raw_response.txt`, `digests/raw_context.txt`

## Where the writing logic lives
There is **zero prose-writing logic in Python**. All wording comes from a Claude model following `SYSTEM_PROMPT` in `digest.py` — a ~150-line editorial brief defining the audience, voice ("calm, clear journalist, no hype"), three-section structure, visual rules, dedup rules, and the exact JSON output schema. Python code only fetches, validates, and mechanically transforms JSON into MD/HTML.

## Digest structure (current, post beginner-friendly rewrite)
Claude outputs JSON wrapped in `<!-- BEGIN_JSON --> ... <!-- END_JSON -->`:
- `teaser` — one sentence for a non-technical reader
- `lead_story` — title, what_happened, what_this_means, visual fields, source
- `quick_hits` — 3–4 short stories, 2–3 sentences each, no jargon
- `under_the_hood` — 1–2 more technical stories, optional ≤10-line code example
- `fun_fact` — punchy one-liner or null
- Visual fields per story: `visual_type` ("image" | "chart" | "table" | null), `visual_url` (must be verbatim from fetched context), `visual_data` (Claude-synthesized headers/rows). Prompt mandates ≥2 visuals per digest.

## Pipeline stages (digest.py, single entry point via main())
1. `load_seen_topics()` — reads `seen_topics.json`, prunes to 7-day window
2. `gather_context()` — scrapes Hacker News, GitHub Trending, HuggingFace Blog, Anthropic News, GitHub Blog (OpenAI blog removed — reliable 403; HN covers it). Enriches top 3 articles per blog source with og:image + first paragraph (parallel, SSRF-guarded). **Fail-loud guardrail:** raises RuntimeError if fewer than 3 of 5 sources return content. Returns `(context, image_refs, known_urls)`. Context capped at 16k chars.
3. `generate_digest()` — single Claude API call (`claude-haiku-4-5-20251001`), no tools
4. `parse_output()` — extracts JSON from delimiters
5. `sanitize_story_urls()` — drops any source_url/visual_url not in `known_urls`. This is the real security boundary against scraped-content prompt injection (the prompt rule alone is not). Guards against non-dict stories.
6. `render_markdown()` + `render_html()` — deterministic rendering; HTML via Jinja2 `template.html` (autoescape on; only `md_links` filter uses `| safe`, and it does its own escaping)
7. `save_files()` → `save_seen_topics()` (only after successful save) → archive regeneration (`build_archive_entries` + `render_archive` → `archive.html`)

Skips entirely if today's digest already exists (rerun-safe).

## The two execution paths — current structural problem
**Local:** `python digest.py` runs the pipeline above; Haiku writes the digest.

**Scheduled (06:45 Europe/Helsinki, Claude Code routine, trigger `trig_01H3NViVVFhGYrTXS4VyNu35`):** the routine does **not** call `main()`. It reimplements pipeline stages as inline `python -c` scripts stored in the trigger config, and the Claude Code agent itself writes the digest JSON — no Haiku API call. This means:
- The pipeline exists twice (main() vs inline trigger steps)
- The editorial brief exists twice (SYSTEM_PROMPT vs trigger prompt)
- Every change to digest.py or the prompt must be manually mirrored, or the paths drift. This has already caused breakage once (cascading failures after security patches).

**Open decision:** unify the paths. Preferred direction: shrink the trigger to "setup env → `python digest.py` → git add/commit/push (`digests/`, `seen_topics.json`, `archive.html`, `index.html`)" so the routine executes the real code. Alternative: keep agent-as-writer but move all step logic into a repo-tracked `ROUTINE.md` the trigger reads — lower drift, not zero.

## Automation details (current)
- Routine commits to a `claude/YYYYMMDD` branch; GitHub Actions workflow (`.github/workflows/auto-merge-claude.yml`) merges main into it, opens a PR, squash-merges, deletes the branch
- Step 7 `git add` must include `archive.html` (repo root, not `digests/`) or the archive silently goes stale
- Manage at https://claude.ai/code/routines

## Deduplication
`seen_topics.json` (repo root, **committed to git** — being gitignored previously caused daily repeats). Rolling 7-day window, pruned on every run, ~42 entries max. Passed to Claude as context; exact repeats skipped, genuine follow-ups prefixed "Previously covered on {date}: ...".

## Files
- `digest.py` — main script, single entry point, contains SYSTEM_PROMPT
- `template.html` — Jinja2 digest template (editorial layout: masthead, hero with lead story + sticky Quick Hits sidebar, Quick Hits accordion via `<details>`, 2-col Under the Hood, Fun Fact strip; Newsreader + IBM Plex; forest-green palette)
- `archive_template.html` — Jinja2 archive template
- `index.html`, `assets/favicon.svg`
- `seen_topics.json` — committed dedup memory
- `CLAUDE.md` — Claude Code session instructions (env setup, model constraint, no-API-call testing recipes)
- `.github/workflows/auto-merge-claude.yml`
- `requirements.txt` — anthropic, requests, beautifulsoup4, python-dotenv, jinja2

## Constraints & principles
- **Fail loud**: abort with informative errors rather than emit a hollow digest (source-count guardrail, RuntimeError on API failure)
- **Model**: `claude-haiku-4-5-20251001` only — cost constraint (~$0.01–0.03/run)
- Self-fetch headlines instead of web_search tool (cost control, context control)
- Windows dev environment, venv mandatory
- Only env var: `ANTHROPIC_API_KEY`

## Resolved (was previously open)
- Beginner-friendly rewrite: **merged** — new SYSTEM_PROMPT, three-section schema, and rendering are live in digest.py
- `sanitize_story_urls` unguarded `data["lead_story"]` access: **fixed** (isinstance guard in place)
- `seen_topics.json` gitignore bug: fixed, file committed
- Email code fully removed

## Next work
1. **Unify the two execution paths** (see open decision above) — the highest-value structural fix
2. Verify remaining allowlist entries for HuggingFace / Anthropic blog in the routine environment (past 403s)
3. Minor: `extract_seen_entries()` assumes `lead["title"]`/`lead["source_url"]` exist — could KeyError on malformed output (low priority; runs after render already succeeded)
4. Backlog (FUTURE.md): archive page polish, PWA support, push notifications, search across digests
