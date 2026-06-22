# Daily Tech Digest — Monday, June 22 2026

> The AI that quietly pulls the numbers for you is arriving at work — and the plumbing behind it is getting a lot cheaper to run.

---
## GitHub Built an AI That Lets Any Employee Query Company Data in Plain English

**What happened**
GitHub described how it built Qubot, an internal assistant that lets any employee ask questions about company data in plain English and get an answer back — instead of waiting on a data team to write the database query.

**What this means**
This is the shape of AI most professionals will actually meet at work: not a chatbot to talk to, but a colleague that fetches the numbers for you. For managers, marketers, and operations staff, it means self-serve answers without learning to write queries or filing a request — and it's a strong hint your own company may roll out something similar.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/)

---
## Quick Hits

### A Fully Open AI Model Pitches 'Sovereign AI' for Anyone Who Wants Control

A new foundation model called Apertus has been released with fully open weights, aimed at "sovereign AI" — countries and organisations running capable models they own and control rather than renting access from a handful of US firms. Because the weights are open, anyone can inspect it, fine-tune it, and host it on their own machines.

Source: [Apertus ↗](https://apertvs.ai/)

### GitHub Copilot Switches to Pay-As-You-Go Pricing

GitHub is moving Copilot, its widely used AI coding assistant, to usage-based billing: your activity now draws down "GitHub AI Credits" instead of a flat monthly fee. Heavy users will likely pay more and light users less. It's another sign that flat-rate AI subscriptions are giving way to metered use you have to keep an eye on.

Source: [GitHub Blog ↗](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

### A Free Dashboard Tries to Replace Doomscrolling With One Calm Screen

WorldMonitor, a free open-source project, pulls global news, geopolitical events, and infrastructure status into a single real-time dashboard and uses AI to summarise and flag what actually matters. It's pitched as a personal situational-awareness screen rather than yet another feed to scroll through.

Source: [GitHub Trending ↗](https://github.com/koala73/worldmonitor)

### An Open Tool Gives AI Assistants a Long-Term Memory

Cognee is an open-source tool that gives AI assistants memory across sessions, so they remember earlier context instead of starting from scratch every conversation. It stores what they learn in a private, self-hosted knowledge graph — useful for anyone building an assistant that needs to remember past work rather than forget it overnight.

Source: [GitHub Trending ↗](https://github.com/topoteretes/cognee)

---
## Under the Hood

### A Tool That Squeezes 60–95% of the Cost Out of AI Requests

**What happened**
Headroom sits between your application and a large language model and compresses what gets sent in — tool outputs, logs, files, and retrieved document chunks — reporting 60 to 95 percent fewer tokens while keeping the same answers. It ships three ways: a Python library, a proxy, or an MCP server.

**Why it matters**
Tokens are what you pay for, so cutting the input by more than half directly cuts the bill and frees up room in the model's limited context window for the parts that matter. For teams running AI features at scale, that can be the difference between a feature that's affordable to keep and one that gets cut.

Source: [GitHub Trending ↗](https://github.com/chopratejas/headroom)

### A Modern Rewrite of SQLite, the Database Hiding in Your Phone

**What happened**
Turso is an in-process SQL database compatible with SQLite — it runs inside your app rather than as a separate server — but it's being rebuilt from scratch in Rust to add features SQLite has long lacked, such as better handling of simultaneous writes and built-in syncing.

**Why it matters**
SQLite is one of the most widely deployed pieces of software on the planet, quietly running inside phones, browsers, and countless apps. A drop-in, modernised alternative matters to developers who want SQLite's zero-setup simplicity without bumping into its old limits.

Source: [GitHub Trending ↗](https://github.com/tursodatabase/turso)

---
**Fun fact:** Someone built a website that lets you pull any of 1,247 Criterion films off a virtual shelf.

*Daily tech digest for curious professionals. AI news that affects your work.*