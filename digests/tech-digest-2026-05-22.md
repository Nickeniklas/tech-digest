# Daily Tech Digest — Friday, May 22 2026

> Google's own Chrome DevTools team published an official AI agent plugin — your coding assistant can now see exactly what your browser sees when something breaks.

---
## Chrome DevTools Is Now an Official Tool for AI Coding Assistants

**What happened**
Google's Chrome DevTools team published an official MCP server — a standardized plugin that connects AI coding assistants like Claude Code directly to Chrome's browser debugger, console, network inspector, and performance profiler. Instead of manually copying error messages into a chat window, your AI assistant can now read live browser output directly.

**What this means**
This closes a real gap: AI tools could read your code but couldn't observe what the browser was actually doing at runtime. If you build, maintain, or test websites — or work alongside someone who does — AI assistants just got meaningfully more capable at catching what's wrong without needing you to relay information back and forth.

Source: [GitHub / ChromeDevTools ↗](https://github.com/ChromeDevTools/chrome-devtools-mcp)

---
## Quick Hits

### An Open-Source Platform Wants to Make AI Agents Feel Like Real Teammates

Multica launched on GitHub as a free, open-source platform for managing AI coding agents like a team — assign them tasks, track their progress, and let them accumulate skills over time. The goal is to replace one-off AI chat sessions with something closer to a persistent, capable colleague you can delegate to. It supports Claude Code, Codex, and other agents out of the box.

Source: [GitHub / multica-ai ↗](https://github.com/multica-ai/multica)

### NotebookLM's Hidden Features Are Now Accessible via Python

A developer published an unofficial Python API for Google NotebookLM that unlocks capabilities the web interface doesn't expose — including automated notebook creation, source management, and programmatic audio generation. You can now build NotebookLM into larger workflows or automate tasks you'd otherwise have to do by hand in the browser.

Source: [GitHub / teng-lin ↗](https://github.com/teng-lin/notebooklm-py)

### A New Tool Turns Any Codebase Into an Interactive Map You Can Explore and Query

Understand-Anything generates a navigable knowledge graph from any codebase — you can search it, explore relationships between components, and ask it questions directly. It connects to Claude Code, Cursor, Copilot, and Gemini CLI. For anyone who's ever inherited an unfamiliar project and had no idea where to start, this is the kind of tool that makes that situation much less overwhelming.

Source: [GitHub / Lum1104 ↗](https://github.com/Lum1104/Understand-Anything)

### Microsoft's .NET Team Published Official AI Agent Skills for C# Developers

Microsoft's .NET team released a public skills repository designed to help AI coding agents work correctly with .NET and C# projects. These instruction files teach AI tools the conventions, idioms, and quirks of the .NET ecosystem — and having them come from the language's own maintainers gives them an authority that community-built versions can't match.

Source: [GitHub / dotnet ↗](https://github.com/dotnet/skills)

---
## Under the Hood

### Forge: A Minimal Python Framework for Self-Hosted AI Workflows

**What happened**
Forge is a new Python framework for building multi-step AI workflows and tool-calling pipelines that run on your own infrastructure rather than through a managed cloud service. It handles chains of LLM calls and agent loops while staying deliberately lightweight — the whole framework is designed around the idea that simpler architecture is easier to debug and control.

**Why it matters**
Most agentic frameworks (LangChain, AutoGen, CrewAI) have grown complex enough that debugging a broken workflow can be harder than writing one from scratch. Forge bets on minimalism: less magic, more transparency. For teams building production AI pipelines who've hit the limits of heavier frameworks, it's worth evaluating against your specific use case.

Source: [GitHub / antoinezambelli ↗](https://github.com/antoinezambelli/forge)

---
**Fun fact:** The Chrome DevTools MCP server is the first official browser debugging tool designed from the ground up to be used by an AI agent, not a human.

*Daily tech digest for curious professionals. AI news that affects your work.*