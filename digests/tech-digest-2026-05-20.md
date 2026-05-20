# Daily Tech Digest — Wednesday, May 20 2026

> Anthropic just published an official, vetted directory of Claude Code plugins — and a new open-source tool claims to cut your AI API costs by up to 90% by stripping unnecessary tokens before they reach the model.

---
## Anthropic Publishes an Official Directory of Claude Code Plugins

**What happened**
Anthropic released a new GitHub repository called claude-plugins-official — a curated, Anthropic-managed directory of high-quality plugins for Claude Code, the company's AI coding assistant.

**What this means**
Until now, finding trustworthy Claude Code extensions meant searching GitHub and hoping for the best. This gives teams a vetted starting point — plugins reviewed and listed by Anthropic itself, not random developers. If your workplace uses Claude Code, this is now the first place to look before adding any new capability.

Source: [GitHub Trending ↗](https://github.com/anthropics/claude-plugins-official)

---
## Quick Hits

### New Tool Cuts AI API Token Usage by 60–90%

A developer released rtk — a lightweight CLI proxy written in Rust that sits between your terminal and an AI model, automatically stripping redundant tokens before they reach the API. The developer claims 60–90% reduction on common development commands, which translates directly into lower API bills. It installs as a single binary with no dependencies.

Source: [GitHub Trending ↗](https://github.com/rtk-ai/rtk)

### AI Video Tool Combines Director, Writer, and Producer Into One Pipeline

HKUDS released ViMax, an open-source AI video generation system that handles the full creative pipeline — scripting, directing, producing, and rendering — in a single automated workflow rather than requiring separate tools stitched together. It's early research software rather than a polished product, but it shows how AI video creation is moving from single-step generation toward full-production automation.

Source: [GitHub Trending ↗](https://github.com/HKUDS/ViMax)

### Free Patch Turns GIMP Into a Photoshop Lookalike

PhotoGIMP is an open-source patch for GIMP 3 that remaps the interface, keyboard shortcuts, and toolbar layout to match Adobe Photoshop. For designers, teachers, or marketers who know Photoshop but want to avoid a subscription, it significantly lowers the learning curve of switching. GIMP is free; this patch makes it feel familiar.

Source: [GitHub Trending ↗](https://github.com/Diolinux/PhotoGIMP)

### Open-Source Project Lets You Run Claude Code for Free

A developer published free-claude-code, a project that routes Claude Code through alternative endpoints so it works without a paid Anthropic subscription — in the terminal, the VS Code extension, or Discord, with voice support included. This is a community workaround, not an official Anthropic product, and users should review terms of service implications before using it professionally.

Source: [GitHub Trending ↗](https://github.com/Alishahryar1/free-claude-code)

---
## Under the Hood

### Andrej Karpathy's AI Coding Pitfalls, Distilled Into a Single Config File

**What happened**
A developer published a single CLAUDE.md file derived from Andrej Karpathy's — the AI researcher and former Tesla AI director — publicly documented observations about where language models reliably fail at coding tasks. The file is designed to drop into any project and immediately improve Claude Code's behaviour.

**Why it matters**
CLAUDE.md files act as standing instructions for AI coding agents — they shape how the model approaches a codebase before writing a single line. Rather than writing behavioural rules from scratch, developers get a peer-reviewed starting point built from one of the field's most respected researchers. The four recurring pitfalls Karpathy identified: overconfidence (not flagging uncertainty), context blindness (ignoring existing code patterns), hallucinated APIs (inventing function names), and scope creep (modifying more than asked).

```python
# Drop into your project root as CLAUDE.md
# Derived from Andrej Karpathy's LLM coding pitfall observations
# Source: github.com/multica-ai/andrej-karpathy-skills

## Rules
- Flag uncertainty explicitly before writing code
- Read existing patterns before introducing new ones
- Never invent API names — check docs first
- Change only what was asked; nothing more
```

Source: [GitHub Trending ↗](https://github.com/multica-ai/andrej-karpathy-skills)

---
**Fun fact:** PhotoGIMP turns the world's oldest free image editor into a convincing Photoshop replacement — for zero dollars.

*Daily tech digest for curious professionals. AI news that affects your work.*