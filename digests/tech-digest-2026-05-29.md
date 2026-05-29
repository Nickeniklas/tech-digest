# Daily Tech Digest — Friday, May 29 2026

> Microsoft open-sourced a tool that converts any Office document or PDF to Markdown — making your files instantly usable in AI workflows.

---
## Microsoft's Document Converter Makes Your Files AI-Ready

**What happened**
Microsoft released markitdown, a free Python tool that converts virtually any file format — Word documents, PowerPoint presentations, Excel spreadsheets, PDFs, and more — into Markdown. Markdown is the plain-text format that AI assistants handle best.

**What this means**
If you regularly paste documents into AI tools and find the formatting gets garbled, markitdown solves that. Teachers uploading lesson plans, lawyers working with contracts, marketers editing briefs — anyone who feeds files into AI assistants can now do it cleanly.

Source: [GitHub ↗](https://github.com/microsoft/markitdown)

---
## Quick Hits

### Anthropic Published a Public Skills Library for AI Agents

Anthropic opened a public GitHub repository called 'skills' — a collection of reusable capabilities that AI agents like Claude can use to perform structured tasks. Think of it as a shared toolbox that developers can draw from when building AI-powered tools, rather than reinventing common capabilities from scratch.

Source: [GitHub ↗](https://github.com/anthropics/skills)

### An Open-Source Speech Model Aims for Studio-Quality Voice Generation

The OpenMOSS team released MOSS-TTS, a free family of models for generating realistic speech and sound. It's designed for long-form narration, multiple speakers in one audio, and complex real-world scenarios — all without a cloud subscription or per-minute fees.

Source: [GitHub ↗](https://github.com/OpenMOSS/MOSS-TTS)

### A Web Crawler Built for AI Projects Is Trending

Crawl4AI is an open-source web crawler that delivers website content in a format AI tools can actually use, rather than messy raw HTML. It's become a popular starting point for developers building AI research, monitoring, or content-processing tools.

Source: [GitHub ↗](https://github.com/unclecode/crawl4ai)

### A New Plugin Brings Compound Engineering to Every Major AI Coding Tool

Every Inc. released an official plugin for an approach called compound engineering, built to work across Claude Code, GitHub Copilot, Cursor, and Codex. The idea: chain multiple AI reasoning steps into a coordinated task rather than relying on one-shot prompts, so each step builds on the last.

Source: [GitHub ↗](https://github.com/EveryInc/compound-engineering-plugin)

---
## Under the Hood

### A Meta-Skill Designs Entire AI Agent Teams Automatically

**What happened**
A developer published 'harness' — a meta-skill for AI coding agents that takes a domain description and generates a full team of specialized sub-agents, each with defined roles and skill sets. Instead of prompting a single AI to do everything, you get purpose-built agents for each part of the workflow.

**Why it matters**
This reflects a broader shift in AI tooling toward multi-agent systems where specialized AIs handle distinct parts of a task. Harness automates the hardest part — designing the team structure itself — which previously required significant manual prompt engineering and iteration.

```python
# Describe your domain, get a purpose-built agent team
harness.design(
  domain="legal document review",
  tasks=["clause extraction", "risk flagging", "summary"]
)
# Returns 3 specialized agents with defined skill sets
```

Source: [GitHub ↗](https://github.com/revfactory/harness)

---
**Fun fact:** markitdown converts Word, Excel, PowerPoint, PDFs, images, and audio files into AI-ready plain text.

*Daily tech digest for curious professionals. AI news that affects your work.*