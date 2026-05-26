# Daily Tech Digest — Tuesday, May 26 2026

> Garry Tan's personal AI setup is now public — and it runs like a whole business team, not a single assistant.

---
## Garry Tan's Personal Claude Code Setup Is Now Public

**What happened**
Y Combinator president Garry Tan published gstack, his full Claude Code configuration, on GitHub. It includes 23 specialized tools, each assigned a distinct professional role: CEO, Designer, Engineering Manager, Release Manager, Documentation Engineer, and QA tester.

**What this means**
This offers a direct look at how a prominent Silicon Valley executive structures AI assistance — treating it not as one generalist helper but as a coordinated team of specialists. For professionals using AI tools, the pattern of assigning distinct roles to different AI configurations is likely to influence how non-coding platforms are designed next.

Source: [GitHub ↗](https://github.com/garrytan/gstack)

---
## Quick Hits

### A New Tool Removes AI Tells from Your Writing

Developer Hardik Pandya published stop-slop, a skill file for AI writing assistants that strips out the phrases and patterns that make AI-generated prose immediately recognizable. If you use AI to help draft emails, reports, or content, it rewrites the output to sound more naturally human — without manual editing on your part. It works with Claude Code and similar tools.

Source: [GitHub ↗](https://github.com/hardikpandya/stop-slop)

### Give Your AI Assistant Better Aesthetic Judgment

Taste-Skill is a new configuration file for AI assistants that pushes them toward more refined, specific outputs rather than generic, template-looking results. The project targets a familiar frustration: AI tools often produce technically correct but creatively flat work — marketing copy that sounds like every other AI draft, or layouts that look like a default theme. Works with Claude Code, Cursor, and similar tools.

Source: [GitHub ↗](https://github.com/Leonxlnx/taste-skill)

### The Open-Source Document Manager That Replaces Your Filing Cabinet

Paperless-ngx — a free, self-hosted document management system — is trending on GitHub this week. It lets you scan, index, and search all your documents from one interface, stored entirely on your own hardware. It's a practical option for professionals who want to cut cloud storage costs or keep sensitive documents off third-party servers.

Source: [GitHub ↗](https://github.com/paperless-ngx/paperless-ngx)

### A Self-Hosted AI Companion Can Now Chat, Remember You, and Play Games

Airi is an open-source AI companion system you can run entirely on your own hardware. It supports real-time voice conversations, can play Minecraft and Factorio autonomously, and runs on web, macOS, and Windows. Unlike cloud AI assistants, all data stays local — and it's designed to feel like a persistent, personalizable presence rather than a stateless chat interface.

Source: [GitHub ↗](https://github.com/moeru-ai/airi)

---
## Under the Hood

### ECC: An Agent Harness That Adds Memory, Security, and Specialization to AI Coding Tools

**What happened**
A developer published ECC — a performance optimization layer for AI coding agents including Claude Code, GitHub Copilot, and Cursor. It adds persistent memory across sessions, security guardrails, task-specific 'instincts,' and a research-first mode that gathers context before taking action.

**Why it matters**
Most AI coding agents reset context every session, have no built-in security constraints, and treat every task the same way regardless of domain. ECC layers all three capabilities onto existing agents without replacing them — making their behavior more consistent and predictable for teams that rely on them in production workflows.

Source: [GitHub ↗](https://github.com/affaan-m/ECC)

### cmux: A Dedicated macOS Terminal Built for Running Multiple AI Agents at Once

**What happened**
manaflow-ai released cmux, a macOS terminal built on the Ghostty engine with vertical tabs and real-time notification support designed specifically for AI coding agents. It's aimed at developers managing several AI agents running in parallel, each handling a different task.

**Why it matters**
Standard terminals weren't built for monitoring multiple concurrent AI agents — they get cluttered fast when each agent is producing its own output stream. cmux treats AI agents as first-class workflow citizens, with dedicated UI affordances that general-purpose terminals don't offer. It's macOS-only for now, but it signals a broader shift: as AI agents multiply, so will the tools for managing them.

Source: [GitHub ↗](https://github.com/manaflow-ai/cmux)

---
**Fun fact:** A new tool targets the handful of phrases that make nearly all AI-generated writing sound identical.

*Daily tech digest for curious professionals. AI news that affects your work.*