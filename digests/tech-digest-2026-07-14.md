# Daily Tech Digest — Tuesday, July 14 2026

> Japan found a way to reclaim most of the lithium from dead EV batteries, Telegram's link domain went dark, and someone built a working neural network in pure SQL.

---
## Japan Finds a Way to Reclaim Most of the Lithium in Dead EV Batteries

**What happened**
Researchers in Japan demonstrated a process that recovers up to 90% of the lithium from spent electric-vehicle batteries, far more than most recycling methods manage today.

**What this means**
Lithium is one of the costliest and most contested materials in modern manufacturing. Reclaiming most of it from old batteries could ease supply pressure and lower long-term costs for anyone whose work touches EVs, electronics, or the shift to cleaner energy.

Source: [Supercar Blondie Tech ↗](https://tech.supercarblondie.com/japan-recovers-up-to-90-of-lithium-from-used-ev-batteries/)

---
## Quick Hits

### Telegram's Link Domain, t.me, Has Been Suspended

The t.me web address, the short link behind virtually every shared Telegram group, channel, and invite, is showing as suspended in domain records. If it stays down, the countless t.me links scattered across the web could stop working, even as the app itself keeps running.

Source: [Whois ↗](https://www.whois.com/whois/t.me)

### California May Force Social Apps to Switch Off 'Infinite Scroll' for Teens

A proposed California law would require platforms to disable engagement features like endless feeds and autoplay for users under 18. Supporters argue the always-more design is built to keep young people hooked. Because so many companies follow California's lead, a change here would likely ripple far beyond the state.

Source: [SFGate ↗](https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php)

### A Rare Look at How Microsoft Gave Its Own Staff AI Coding Tools

Researchers published a study of Microsoft's early-2026 rollout of two AI command-line coding assistants, Claude Code and GitHub Copilot CLI, to its developers. It's an unusually detailed account of how these tools actually land inside a large organization, useful reading for any leader weighing an AI rollout of their own.

Source: [arXiv ↗](https://arxiv.org/abs/2607.01418)

### One Place to Compare Uber, Lyft, Waymo, and Robotaxi Prices

A new tool called Hackney lets you check the cost of the same trip across Uber, Lyft, Waymo, and other robotaxi services side by side. As driverless cabs expand into more cities, it's a simple way to see whether the robot ride is actually the cheaper option.

Source: [Hackney ↗](https://hackney.app/)

---
## Under the Hood

### How GitHub Made Its Issues Pages Feel Instant

**What happened**
GitHub's engineering team rebuilt navigation for its Issues pages so moving between them feels immediate. They leaned on three web techniques: client-side caching (reusing data already loaded), smart prefetching (quietly loading the next page before you click), and service workers (a background layer that can serve pages from a local cache).

**Why it matters**
These are the same tricks that separate a snappy web app from a sluggish one. For anyone building or commissioning web software, it's a concrete example of how perceived speed comes from anticipating the user, not just buying faster servers.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

### Someone Built a Neural Network Entirely in SQL

**What happened**
A developer implemented a working neural network, the math behind modern AI, using nothing but SQL, the decades-old language designed for querying databases. The demo trains on MNIST, the classic collection of handwritten-digit images, entirely inside database queries.

**Why it matters**
It's a playful proof that SQL is far more capable than its 'just fetch some rows' reputation suggests. For data teams, it's a reminder that a lot of number-crunching can happen right where the data already lives, without shipping it off to a separate system.

Source: [GitHub ↗](https://github.com/xqlsystems/xarray-sql/blob/claude/xarray-sql-mnist-demo/benchmarks/nn.py)

---
**Fun fact:** A working neural network, the math behind modern AI, has now been built entirely in SQL, a language meant for querying databases.

*Daily tech digest for curious professionals. AI news that affects your work.*