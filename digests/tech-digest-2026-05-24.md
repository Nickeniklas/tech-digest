# Daily Tech Digest — Sunday, May 24 2026

> A free, open-source AI presentation tool just arrived to challenge paid favorites like Gamma — and NVIDIA dropped infrastructure for long AI-generated video.

---
## A Free, Open-Source AI Presentation Generator Challenges Gamma and Beautiful.ai

**What happened**
Presenton launched on GitHub as a free, self-hostable alternative to paid AI presentation tools like Gamma, Beautiful.ai, and Decktopus. It includes an API, meaning it can be integrated into existing workflows or internal tools.

**What this means**
If your team pays a monthly subscription for an AI slide tool, Presenton offers a no-cost alternative you can run on your own server. For marketers, teachers, and consultants who regularly produce presentations — especially in organizations with data privacy requirements — a self-hosted option is worth a serious look.

Source: [GitHub ↗](https://github.com/presenton/presenton)

---
## Quick Hits

### 754 Cybersecurity Skills Released for AI Coding Assistants

A developer published a library of 754 structured cybersecurity skills for AI coding agents, mapped to five major frameworks including MITRE ATT&CK and NIST. The skills work with Claude Code, GitHub Copilot, Cursor, Gemini CLI, and 20 other platforms. Security and IT teams who use AI assistants can now give those assistants a structured, framework-aligned security vocabulary out of the box.

Source: [GitHub ↗](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

### NVIDIA's Research Lab Published Infrastructure for Long AI-Generated Video

NVIDIA NV Labs released LongLive 2.0, an open-source infrastructure package for generating extended, coherent AI video — the kind of long-form output current tools consistently struggle to produce. The release suggests the technical barriers to long AI video are falling quickly, which will matter for teams in marketing, education, and media production.

Source: [GitHub ↗](https://github.com/NVlabs/LongLive)

### The Interactive Code Map Tool Now Works With Every Major AI Coding Assistant

Previously covered on 2026-05-22: Understand-Anything turns any codebase into a navigable knowledge graph you can search and ask questions about. Since then, the project updated to explicitly support Claude Code, Codex, Cursor, GitHub Copilot, and Gemini CLI — meaning it now slots into whichever AI coding assistant your team already uses.

Source: [GitHub ↗](https://github.com/Lum1104/Understand-Anything)

---
## Under the Hood

### Jane Street Open-Sourced a Tool That Records Every Function Call Your Program Makes

**What happened**
Jane Street, the quantitative trading firm known for its rigorous engineering culture, released magic-trace — a tool that uses Intel's hardware tracing capability to capture a complete, high-resolution recording of every function a program calls. You attach it to any running process and get a full execution timeline you can replay and explore.

**Why it matters**
Most debugging tools tell you a program crashed or slowed down. magic-trace tells you exactly what it was doing in the microseconds before — using CPU-level hardware tracing rather than slower software instrumentation. For developers chasing intermittent bugs or performance regressions, it turns a day-long investigation into a five-minute replay. The fact that Jane Street uses this internally for latency-sensitive trading code is a meaningful quality signal.

```python
# Attach to a running process by PID
magic-trace attach -pid 12345

# Trace a command from the start
magic-trace run ./my-server -- --port 8080

# Result opens automatically in Perfetto trace viewer
```

Source: [GitHub ↗](https://github.com/janestreet/magic-trace)

---
**Fun fact:** Jane Street, Wall Street's most engineering-obsessed trading firm, built magic-trace to debug nanosecond trading code.

*Daily tech digest for curious professionals. AI news that affects your work.*