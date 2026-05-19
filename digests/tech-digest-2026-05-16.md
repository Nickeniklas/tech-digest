# Daily Tech Digest — Saturday, May 16 2026

> Anthropic just made its official AI skills library public — and a new tool can turn any YouTube video, PDF, or webpage into a podcast, quiz, or mind map.

---
## Anthropic Opens Its Agent Skills Library to the Public

**What happened**
Anthropic published a public GitHub repository called 'skills' — an official, curated collection of reusable agent skills for Claude, the same kind used internally to teach Claude specialized behaviors.

**What this means**
Anyone using Claude at work can now browse and apply pre-built skills to customize how Claude behaves — without writing instructions from scratch. This is particularly useful for teams in marketing, research, finance, and engineering who want Claude to follow consistent, professional workflows.

Source: [GitHub ↗](https://github.com/anthropics/skills)

---
## Quick Hits

### Claude Can Now Build Your Automation Workflows for You

A new open-source tool called n8n-mcp connects Claude, Cursor, and Windsurf directly to n8n — one of the most popular no-code automation platforms. Instead of designing a workflow yourself, you describe what you want and Claude builds it. It works with n8n's 400-plus app integrations, covering everything from Slack and Google Sheets to databases and email.

Source: [GitHub ↗](https://github.com/czlonkowski/n8n-mcp)

### Turn Any Webpage, Video, or PDF Into a Podcast, Quiz, or Mind Map

A new Claude skill converts almost any content — web articles, YouTube videos, PDFs, Markdown files, or search results — into formats that Google's NotebookLM can turn into podcasts, slide decks, mind maps, and quizzes. Teachers and researchers who already use NotebookLM get a much faster pipeline for feeding it material from across the web.

Source: [GitHub ↗](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)

### Bun, the All-in-One JavaScript Tool, Is Trending Again

Bun — a JavaScript runtime that replaces Node.js, plus a bundler, test runner, and package manager all in one download — is back on GitHub's trending list. It consistently runs JavaScript significantly faster than standard tools, and developers are increasingly adopting it to speed up web projects without changing their code.

Source: [GitHub ↗](https://github.com/oven-sh/bun)

---
## Under the Hood

### How the n8n-MCP Bridge Actually Works

**What happened**
The n8n-mcp project is an MCP (Model Context Protocol) server — a standardized interface that gives AI tools like Claude, Windsurf, and Cursor the ability to interact with external systems as built-in features. Connected to n8n, Claude can read existing workflows, create new ones, modify individual nodes, and trigger automations mid-conversation.

**Why it matters**
MCP servers are quickly becoming the standard extension layer for AI coding assistants. This one matters because n8n sits on top of over 400 app integrations — so a properly configured setup means Claude can orchestrate complex cross-platform automations from a single prompt. For developers building AI-powered tooling, this is a useful pattern to understand.

```python
// Add to Claude Code's .claude/settings.json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "N8N_URL": "http://localhost:5678",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

Source: [GitHub ↗](https://github.com/czlonkowski/n8n-mcp)

---
**Fun fact:** The n8n automation platform connects over 400 apps — Claude can now build and trigger those workflows just from a chat prompt.

*Daily tech digest for curious professionals. AI news that affects your work.*