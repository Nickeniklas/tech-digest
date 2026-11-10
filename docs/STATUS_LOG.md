# Status log — tech-digest

Session history and dated status notes moved out of `CLAUDE.md` (which holds
current state only). Newest first. Quoted text under each date is verbatim from
`CLAUDE.md`. Where the original text gave only a month ("July 2026"), the day
comes from the git commit that made the change, noted in the heading.

## 2026-11-10 — CLAUDE.md cleanup

- Dated status text moved here from `CLAUDE.md`; `CLAUDE.md` now has a single
  Status section. Current-state claims re-checked against the code (see the
  Status section in `CLAUDE.md`).
- Dated lines then moved out of that new Status section (same day):

> Checked against the code and git refs on 2026-11-10.

> - **Last digest on `origin/main`:** 2026-09-18, as of the last local fetch
>   (2026-09-18). `origin/main` has no digests for 2026-09-05 through 2026-09-17,
>   and nothing after 2026-09-18 can be seen locally. Whether the routine is still
>   running is unverified; check https://claude.ai/code/routines and `git fetch`.
> - **Local `main`** is 1 commit behind `origin/main`; `git pull` before working.

- Follow-up the same day: `git fetch` showed the routine had kept running —
  `origin/main` had 54 new daily digests (2026-09-18 → 2026-11-10), pulled
  fast-forward. The 2026-09-05 → 09-17 gap is real. `render_markdown` was
  hardened against malformed model output (`normalize_digest_data`,
  `tests/test_finish_stage.py`), and the stray test pages
  `digests/test-redesign.html` and `digests/_test_accordion.html` were deleted.

## 2026-07-19 (commits f12df1f, 88564a9, 540d2f3)

From the Scheduling gotcha (local edits to generated files vs. the routine's
morning commit):

> Happened once, July 19 2026, when a PWA/template change sat uncommitted overnight.

From Architecture, stage 1.5 (sources):

> GitHub Trending was dropped as a source in July 2026 — GitHub blocks `/trending`
> scraping origin-side (not a routine-environment proxy issue; `github.com` stays
> allowlisted for git push, and `github.blog` is unaffected), and it was a
> permanently dead source rather than an intermittent failure.

From Architecture, stage 7 (index/archive):

> As of July 2026, `index.html` is no longer a meta-refresh redirect to
> `digests/tech-digest-{date}.html` — it *is* the latest digest, verbatim. iOS
> "Add to Home Screen" bookmarks the current page's URL, so a redirect page
> would permanently pin whatever date happened to be live when the user added
> it. Serving the content at the root instead means the bookmark always shows
> today's digest.

## 2026-07-17 (commit 7c3c593)

From Architecture, stage 1.5 (Anthropic News URL). The allowlist change was made
in the routine environment, not in git; the day is from the commit that
switched the fetch URL to `www`:

> `www.anthropic.com`
> is on the routine environment's allowlist (added July 2026).

From Architecture, stage 6 (`source_urls` must be `[]`, never `[None]`):

> Fixed July 2026; entries written before then age out of the 7-day window on their own.

## 2026-07-16 (commit c652f60)

From Scheduling:

> As of the July 2026 pipeline-unification pass, all pipeline logic lives in
> `digest.py` — the trigger config no longer contains any inline `python -c`
> pipeline steps.

From Architecture (after the description of the three invocation modes):

> Since both the local API path and the scheduled routine call these same two
> functions, there is exactly one implementation of each pipeline stage — nothing
> to keep in sync by hand across two code paths anymore.
>
> The six logical stages below are unchanged in behavior from before the CLI
> refactor — only how they're invoked (directly in `main()` vs. via the `gather`/
> `finish` subcommands) changed:
