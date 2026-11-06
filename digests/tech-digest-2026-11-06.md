# Daily Tech Digest — Friday, November 6 2026

> Anthropic's newest model promises top-tier work for 40% less, and a bug report claims Claude Code shares your email address with websites.

---
## Anthropic releases Claude Opus 5.5, cheaper to run than Opus 5

**What happened**
Anthropic introduced Claude Opus 5.5, the first model in its new Claude 5.5 family. The company says it performs at the level of Claude Fable 5.1 on most work, leads in agentic coding and knowledge work, and costs 40% less to run than Opus 5 on typical workloads.

**What this means**
If your team pays for Claude, the same kind of work — drafting, research, analysis, coding help — should get cheaper without a drop in quality. That makes it easier to justify using AI for everyday tasks rather than saving it for special projects.

Source: [Anthropic ↗](https://www.anthropic.com/claude-opus-5-5)

---
## Quick Hits

### Bug report: Claude Code sends your email address to websites

A widely discussed GitHub issue on Anthropic's Claude Code repository is titled 'Claude Code sends your email address to websites'. If you use AI assistants that browse the web on your behalf, it's a reminder to check what personal details they pass along.

Source: [GitHub ↗](https://github.com/anthropics/claude-code/issues/107757)

### Mark Cuban: Facebook knowingly runs AI deepfake scam ads

Mark Cuban says Facebook knowingly runs scam ads built on AI deepfakes — fake videos of real people — and the report cites documents pointing to $16 billion in fraud-related revenue. If you see a celebrity endorsing an investment in your feed, treat it with suspicion.

Source: [Yahoo Finance ↗](https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html)

### Accessibility statements now have a home on GitHub

GitHub now highlights ACCESSIBILITY.md files, where project owners can describe accessibility goals, known barriers, supported environments and how to report problems. If you rely on assistive technology, or buy software for people who do, this makes it easier to see how seriously a project takes accessibility.

Source: [GitHub Blog ↗](https://github.blog/open-source/maintainers/accessibility-statements-now-have-a-home-on-github/)

### Phonon: speech that runs entirely on your device

Phonon is a small text-to-speech model that turns text into spoken audio on your own device, with no server or internet connection — so what you type stays with you. Its makers say it tops speech-quality benchmarks, which matters for anyone producing voiceovers or accessible materials from sensitive text.

Source: [Hugging Face ↗](https://huggingface.co/blog/phonon-tts)

---
## Under the Hood

### Inside GitHub's new Git storage built for thousands of agents

**What happened**
GitHub explained its new Git storage architecture, designed so thousands of AI agents can push changes to a single repository at the same time. It builds on GitHub's move of nearly all repositories to Azure, using per-reference quorums — agreement among storage servers for each branch — and object storage so reading code can scale separately from writing it.

**Why it matters**
Version control was built for humans pushing a few times a day. As coding agents multiply, the infrastructure underneath has to handle far more simultaneous changes, and this is a look at how one of the biggest code hosts is preparing.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)

### Firenook rebuilds Firebase's local test tools in Rust

**What happened**
Firenook is a new set of Firebase emulators — local copies of Google's app backend that developers use for testing — written in the Rust programming language. Its creator reports 40× faster writes and 10× less memory use than the standard tools.

**Why it matters**
Faster, lighter test environments shorten the wait between making a change and seeing whether it works, which adds up for teams (and AI coding agents) running tests constantly.

Source: [Firenook ↗](https://firenook.dev/)

---
**Fun fact:** One team says it trained a decent text-to-image model for about $20,000 — and gave the weights away.

*Daily tech digest for curious professionals. AI news that affects your work.*