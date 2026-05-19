# Daily Tech Digest — Monday, May 11 2026

> A self-evolving AI agent that teaches itself new skills — and uses six times fewer resources to do it — is turning heads on GitHub this week.

---
## An AI Agent That Learns New Skills on Its Own Is Trending on GitHub

**What happened**
A developer published GenericAgent — an AI agent that begins with a small base of capabilities and autonomously builds out a 'skill tree,' adding new abilities as it encounters new tasks. It claims to handle complex, full-system tasks while using six times fewer tokens than typical agents.

**What this means**
Most AI tools require someone to configure exactly what they can do. An agent that expands its own abilities could take on increasingly varied work — scheduling, research, document drafting — without constant setup. That's a meaningful shift for anyone trying to offload repetitive cognitive tasks.

Source: [GitHub ↗](https://github.com/lsdefine/GenericAgent)

---
## Quick Hits

### Run AI Models Locally on a Mac From the Menu Bar

omlx is a new local LLM server built specifically for Apple Silicon Macs that you manage from the macOS menu bar. It uses SSD offloading to run AI models larger than your available RAM and handles multiple requests at once. For Mac users who want to keep their AI work private and offline without paying per query, this removes a significant barrier.

Source: [GitHub ↗](https://github.com/jundot/omlx)

### A Browser-Based 3D Scene Editor Opens Up for AI-Captured Environments

PlayCanvas released SuperSplat, an open-source in-browser editor for 3D Gaussian Splats — a technique that turns photos or video into navigable 3D scenes. It lets designers edit and refine these AI-generated captures directly in a browser, no software install needed. The technology is quietly becoming part of mainstream creative and visualization workflows.

Source: [GitHub ↗](https://github.com/playcanvas/supersplat)

### A Meta-Layer for AI Coding Agents Adds Memory and Security

A developer released everything-claude-code — a system designed to sit on top of AI coding tools like Claude Code, Cursor, and Codex, adding persistent memory, security guardrails, and smarter research-first behaviors. It works across multiple coding agents, not just one. As AI coding tools become standard in more workplaces, these orchestration layers will shape how safely and effectively they're used.

Source: [GitHub ↗](https://github.com/affaan-m/everything-claude-code)

### A Free Course Teaches How to Build AI Agents From Scratch

Datawhalechina published hello-agents on GitHub — a step-by-step tutorial series that walks complete beginners through building AI agents from first principles. It covers both the theory and the practice of agent design. As autonomous AI workflows become a practical skill for non-engineers, resources like this signal what the next wave of AI literacy will look like.

Source: [GitHub ↗](https://github.com/datawhalechina/hello-agents)

---
## Under the Hood

### How omlx Uses SSD Offloading to Run Large Models on a MacBook

**What happened**
omlx is an inference server tuned for Apple Silicon — the chip in modern Macs — that addresses the core bottleneck of running large language models locally: not enough RAM. It offloads model weights to SSD storage when they exceed available memory, and uses continuous batching to serve multiple requests in parallel rather than processing them one at a time.

**Why it matters**
For developers building or testing local AI applications on a Mac, omlx effectively extends the size of model that's practical to run without expensive hardware upgrades. SSD offloading trades some latency for a much larger model ceiling; continuous batching keeps throughput reasonable even with that tradeoff.

Source: [GitHub ↗](https://github.com/jundot/omlx)

---
**Fun fact:** GenericAgent starts from just 3,300 lines of code and grows its own capabilities from there.

*Daily tech digest for curious professionals. AI news that affects your work.*