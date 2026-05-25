# Daily Tech Digest — Monday, May 25 2026

> Anthropic just published a free plugin library built specifically for teachers, marketers, lawyers, and managers — not developers — and a new AI model arrived that speaks the language of financial markets.

---
## Anthropic Published an Official Plugin Library Built for Knowledge Workers

**What happened**
Anthropic released a new open-source repository called knowledge-work-plugins — an officially managed collection of Claude plugins designed specifically for non-technical professionals: teachers, marketers, lawyers, designers, and managers who use AI in their daily work. It is separate from the developer-focused plugin directory and is publicly available on GitHub.

**What this means**
If you use Claude at work, this is a direct signal from Anthropic that your use case matters as much as a software engineer's. Rather than adapting tools built for coders, you now have a curated, officially supported starting point built around the work you actually do.

Source: [GitHub — anthropics/knowledge-work-plugins ↗](https://github.com/anthropics/knowledge-work-plugins)

---
## Quick Hits

### A New AI Model Was Built to Understand Financial Markets — Not Just Text About Them

Researchers released Kronos, a foundation model trained specifically on financial market data rather than general language. It is designed to recognize the patterns and signals that move prices — a different architecture from asking ChatGPT to summarize a chart. Financial analysts and investment professionals are the likely early users.

Source: [GitHub — shiyu-coder/Kronos ↗](https://github.com/shiyu-coder/Kronos)

### A New Tool Cuts AI Coding Assistant Token Usage — and Keeps Your Code Off the Cloud

CodeGraph is a pre-indexed knowledge graph for your codebase that works with Claude Code, Cursor, GitHub Copilot, and others. Instead of sending large chunks of your code to the AI on every query, it answers from a local index — using fewer tokens and fewer round trips. Everything stays on your machine, which matters when the code is sensitive.

Source: [GitHub — colbymchenry/codegraph ↗](https://github.com/colbymchenry/codegraph)

### A Free, Self-Hosted Home Security System Runs AI Directly on Your Own Hardware

Frigate is an open-source network video recorder that performs real-time object detection on your home hardware — no cloud subscription, no footage leaving your network. It works with standard IP cameras and can distinguish people, cars, and animals in real time. For anyone concerned about smart home privacy, it is a self-hosted alternative to Ring or Google Nest.

Source: [GitHub — blakeblackshear/frigate ↗](https://github.com/blakeblackshear/frigate)

---
## Under the Hood

### pi: One Open-Source Toolkit Bundles a Coding Agent, Slack Bot, Web UI, and Local Model Support

**What happened**
A new open-source project called pi packages multiple AI agent components into a single repository: a coding agent CLI, a unified API layer that works across multiple LLM providers, both terminal and web interfaces, a Slack bot integration, and support for running open-source models locally via vLLM. It is designed for developers who want one coherent stack rather than assembling disparate libraries.

**Why it matters**
Building internal AI agent infrastructure usually means stitching together five or six different libraries. pi consolidates that into one codebase — useful for teams experimenting with deploying AI agents inside a company workflow or product, especially if you want to support both cloud models and self-hosted open-source ones from the same interface.

Source: [GitHub — earendil-works/pi ↗](https://github.com/earendil-works/pi)

---
*Daily tech digest for curious professionals. AI news that affects your work.*