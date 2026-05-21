# Daily Tech Digest — Thursday, May 21 2026

> A new GitHub project packs an entire team of specialized AI workers into one open-source toolkit — each agent playing a different professional role with its own workflow and deliverables.

---
## One Toolkit, A Full AI Team: Each Agent Plays a Different Professional Role

**What happened**
A developer released agency-agents on GitHub — a collection of AI agents where each plays a distinct professional role: frontend developer, Reddit community manager, creative ideator, and fact-checker, each with its own defined personality, workflow, and expected deliverables.

**What this means**
Rather than prompting one general AI to do every task, this lets you summon a specialist — a copy editor who thinks like a marketer, a project manager with its own checklists, a reality-checker for creative work. It's an early signal of how people are starting to organize AI into teams rather than single tools.

Source: [GitHub ↗](https://github.com/msitarzewski/agency-agents)

---
## Quick Hits

### Free, Self-Hosted WhatsApp Automation Is Now One Repository Away

OpenWA launched as a free, open-source WhatsApp API gateway you can run on your own server — no subscription, no per-message fees. For small businesses already living in WhatsApp, it means automating customer replies, appointment reminders, and order notifications without paying for the official Business API.

Source: [GitHub ↗](https://github.com/rmyndharis/OpenWA)

### AI Tools Can Now Remember Your Work Across Every Session

AgentMemory hit GitHub Trending as the self-described #1 persistent memory solution for AI coding agents, backed by real-world benchmarks. It gives tools like Claude Code or Cursor a way to remember your code context, past decisions, and project patterns — so you stop re-explaining your project from scratch every time you open a new session.

Source: [GitHub ↗](https://github.com/rohitg00/agentmemory)

### A Free, Ad-Free Desktop App for Streaming Any Movie or TV Show

Streambert is a new cross-platform desktop app that lets you stream or download movies, TV series, and anime with no ads, no tracking, and no subscription. It runs on Windows, Mac, and Linux.

Source: [GitHub ↗](https://github.com/truelockmc/streambert)

### A Minimal App Gives Your Private Writing Notes a Quiet Home

Files.md is a stripped-down desktop writing app for Markdown notes — designed as a private, distraction-free thinking space with no sync, no account, and no data leaving your device. It's aimed at writers, researchers, and knowledge workers who want a simple private journal without cloud exposure.

Source: [GitHub ↗](https://github.com/zakirullin/files.md)

---
## Under the Hood

### Oh-My-Pi: A Terminal AI Agent With Hash-Anchored Edits, Browser Access, and Parallel Subagents

**What happened**
A developer released oh-my-pi, a terminal-based AI coding agent with an unusually deep feature set: hash-anchored edits (which tie each proposed code change to a specific file state, preventing misapplied patches), a built-in browser for reading live documentation, full LSP integration for language-aware code understanding, and native support for spawning parallel subagents to work on tasks simultaneously.

**Why it matters**
Most AI terminal agents apply edits sequentially with no safety mechanism and no awareness of live docs. Oh-my-pi's architecture treats the terminal as a proper development environment — it knows the exact state of your file before editing, can look things up without leaving the session, and can split work across multiple agents at once. Developers working on large codebases will find this closer to how senior engineers actually work.

Source: [GitHub ↗](https://github.com/can1357/oh-my-pi)

---
**Fun fact:** OpenToonz — the animation software behind Studio Ghibli films — is fully free and trending on GitHub today.

*Daily tech digest for curious professionals. AI news that affects your work.*