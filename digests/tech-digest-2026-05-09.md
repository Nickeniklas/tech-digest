# Daily Tech Digest — Saturday, May 9 2026

> An open-source AI agent that trades stocks entirely on its own is now available to anyone — and Amazon published a structured rulebook for how AI coding agents should handle complex software projects.

---
## A Fully Automated AI Trading Agent Is Now Open Source

**What happened**
Researchers at HKUDS published AI-Trader on GitHub — an AI agent that handles the entire trading cycle without human involvement: it analyzes markets, selects assets, and executes buy and sell orders autonomously.

**What this means**
Autonomous trading tools have historically required expensive proprietary infrastructure. Making one open-source puts that capability within reach of smaller firms, fintech startups, and individual developers. If you work in finance, wealth management, or investment advisory, AI-Trader signals a shift toward fully autonomous execution that could change how trading operations are staffed.

Source: [GitHub ↗](https://github.com/HKUDS/AI-Trader)

---
## Quick Hits

### Amazon Published a Rulebook for How AI Coding Agents Should Work

AWS Labs released aidlc-workflows on GitHub — a set of adaptive steering rules that guide AI coding agents through the entire software development lifecycle, from planning through deployment. Think of it as a project management checklist, written for AI agents rather than humans. It's aimed at teams already using AI agents to handle large software projects.

Source: [GitHub (AWS Labs) ↗](https://github.com/awslabs/aidlc-workflows)

### A Modified Browser Passes Every Bot Detection Test on the Market

CloakBrowser is a custom build of Chrome designed to pass the bot-detection tools that websites use to block automated browsing — it passed 30 out of 30 tests from major detection services. It works as a drop-in replacement for Playwright, the tool used widely in web automation, QA testing, and competitive research. The difference from other stealth tools: it patches Chrome at the source code level, making it much harder to detect.

Source: [GitHub (CloakHQ) ↗](https://github.com/CloakHQ/CloakBrowser)

### A Platform for Collaborating With Teams of AI Agents Is Trending

Lobehub is gaining attention on GitHub with a platform designed around working alongside multiple AI agents as if they were team members. You can build and configure specialist agents, assign them roles, and have them hand tasks off to each other. It targets both work productivity and personal projects.

Source: [GitHub (lobehub) ↗](https://github.com/lobehub/lobehub)

---
## Under the Hood

### How CloakBrowser Defeats Bot Detection at the Source Level

**What happened**
Most stealth browsers defeat bot detection by layering JavaScript overrides on top of standard Chrome — spoofing canvas fingerprints, WebGL renderer strings, and font metrics at runtime. Detection services have learned to spot those overrides. CloakBrowser takes a different approach: it patches Chrome's source code directly, so the browser genuinely behaves differently rather than pretending to.

**Why it matters**
Source-level patches are fundamentally harder to detect because there's nothing to override — the fingerprint is real. For QA engineers, data teams, and developers doing competitive research or accessibility testing, this is a meaningful capability jump. It also raises the bar for anti-bot infrastructure across the web, since detection services will need to find new signals.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Point Playwright at CloakBrowser instead of standard Chrome
    browser = p.chromium.launch(
        executable_path='/path/to/cloakbrowser'
    )
    page = browser.new_page()
    page.goto('https://example.com')
    print(page.title())
    browser.close()
```

Source: [GitHub (CloakHQ) ↗](https://github.com/CloakHQ/CloakBrowser)

---
**Fun fact:** CloakBrowser passed 30 out of 30 bot-detection tests, including every major commercial anti-scraping service.

*Daily tech digest for curious professionals. AI news that affects your work.*