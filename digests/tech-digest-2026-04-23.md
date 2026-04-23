# Daily Tech Digest — Thursday, April 23 2026

> Claude Code gets whole-codebase semantic search via MCP, Vercel ships open agent skills, and LLM observability standardizes on OpenTelemetry — peak AI tooling week.

**Today's pick:** claude-context solves the biggest friction in AI-assisted coding: keeping the right files in context without manually curating what your agent sees. Point it at any repo and let the MCP handle retrieval.

---
**Fun fact:** Developers spend 35% of their time navigating code they didn't write — now it's the AI agent's problem.

---
## claude-context: Semantic Whole-Repo Search as an MCP for Claude Code — 🛠️ Dev Tools

**WHAT HAPPENED**
[claude-context](https://github.com/zilliztech/claude-context) is a new MCP server from Zilliz that gives Claude Code agents semantic code search over your entire codebase — no manual file referencing or context stuffing required.

**WHY IT MATTERS**
Context window management is the #1 friction point in AI-assisted coding today. An MCP that handles retrieval automatically means your agent can navigate large repos without you babysitting which files to include in every prompt.

**TRY IT**
```bash
# Add to your Claude Code MCP config (claude_desktop_config.json or .claude/settings.json)
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["-y", "@zilliz/claude-context"]
    }
  }
}
```

Source: [GitHub ↗](https://github.com/zilliztech/claude-context)

---
## Vercel Labs Releases Open Agent Skills Tool — 🛠️ Dev Tools

**WHAT HAPPENED**
[vercel-labs/skills](https://github.com/vercel-labs/skills) is a new open-source project that exposes reusable agent capabilities via a simple `npx skills` CLI, aiming to standardize how AI agents discover and invoke shared skills.

**WHY IT MATTERS**
Skill composition is the unsolved hard problem of agentic AI — if this gains adoption, you can plug verified third-party capabilities into your own agents without building each one from scratch.

**TRY IT**
```bash
npx skills
# Lists available agent skills you can wire into your AI workflows
```

Source: [GitHub ↗](https://github.com/vercel-labs/skills)

---
## Langfuse Adds OpenTelemetry Integration for LLM Observability — 🤖 AI

**WHAT HAPPENED**
[Langfuse](https://github.com/langfuse/langfuse) is trending as one of the top open-source LLM engineering platforms, offering observability, evals, prompt management, and datasets — now with OpenTelemetry support for standardized tracing across your stack.

**WHY IT MATTERS**
OpenTelemetry compatibility means LLM traces can live in the same observability pipeline as the rest of your infrastructure — no more siloed AI monitoring bolted on as an afterthought.

**TRY IT**
```bash
pip install langfuse

from langfuse import Langfuse
langfuse = Langfuse()

trace = langfuse.trace(name="my-llm-call")
span = trace.span(name="generation")
# wrap your LLM call here
span.end(output={"result": response})
```

Source: [GitHub ↗](https://github.com/langfuse/langfuse)

---
## Shannon Lite: Autonomous White-Box AI Pentester for APIs — 🤖 AI

**WHAT HAPPENED**
[Shannon Lite](https://github.com/KeygraphHQ/shannon) is an autonomous AI security tool that reads your source code directly, maps attack vectors, and generates exploit chains to test your own web applications and APIs.

**WHY IT MATTERS**
Traditional pen testing happens infrequently and costs a lot. An AI that continuously red-teams your code as it ships is a meaningful shift — though treat it as a first pass, not a replacement for human security review.

**THE TAKE**
White-box analysis is the right approach here — black-box fuzzing misses too much. The real question is whether teams use this as a continuous gate in CI or a one-off audit tool. The former is where this gets genuinely useful.

Source: [GitHub ↗](https://github.com/KeygraphHQ/shannon)

---
*Daily digest for developers. AI, dev tools, and the occasional hardware drop that actually matters.*