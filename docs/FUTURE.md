# Future Features

- [x] Add visuals — infrastructure complete (enrichment, template rendering for image/chart/table); prompt tuned May 2026 to mandate ≥2 visuals per digest, expose image URLs in a dedicated block at the top of the user message, and clarify that `visual_data` is Claude-synthesized from story numbers rather than waiting for data to appear in source material
- [x] Archive page listing all past digests — `archive.html`, regenerated from the
      `digests/` folder at the end of every `finish_stage()` (both local and routine
      paths). Still v0.1: **not linked from `index.html`**, reachable only by typing
      `/archive.html` directly. Remaining work is polish + linking it, not building it.
- [ ] PWA support (add to home screen, offline reading)
- [ ] Push notifications when new digest drops
- [ ] Search across past digests
- [ ] Styling improvements based on mobile usage
