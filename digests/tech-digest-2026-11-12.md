# Daily Tech Digest — Thursday, November 12 2026

> United Airlines says AI assistants can't book flights for you — one of the first big companies to shut the door on agents acting on a customer's behalf.

---
## United Airlines bans AI agents from booking flights for travelers

**What happened**
United Airlines has barred AI agents — assistants that browse and buy on your behalf — from booking flights for its customers, CBS News reports.

**What this means**
If you've been hoping to hand travel booking to an AI assistant, major airlines may not let it in the door yet. For office managers, assistants and anyone who books trips for others, the human (or the airline's own app) still has to do the clicking for now.

Source: [CBS News ↗](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

---
## Quick Hits

### A personal AI assistant small enough to run on your own device

BotPsy is an AI assistant built on a model with under a billion parameters, small enough to run directly on your phone or laptop instead of in the cloud. Its makers argue that relying on big cloud models means unpredictable costs and a provider that can change or cut off access at any time. Running locally also keeps your data on your device.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/qvac/botpsy)

### Yogurt: a free, private, open-source AI meeting notetaker

A new open-source project called Yogurt pitches itself as a free and private alternative to Granola, the popular AI meeting-notes app. If your organisation is wary of sending meeting recordings to an outside service, tools like this are worth watching.

Source: [GitHub ↗](https://github.com/FrigadeHQ/yogurt)

### Critical security flaw found in Apache, a widely used web server

Security firm Wiz reports a critical flaw in Apache HTTP Server — software that powers a large share of the world's websites — that could let attackers run their own code on affected servers. You don't need to do anything yourself, but expect your IT team or web host to be patching.

Source: [Wiz ↗](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability)

### Google launches the Gemini Decisions API

Google has announced a Gemini Decisions API for developers, a tool aimed at having AI make choices rather than write text. It follows a similar push from Hugging Face earlier this week, a sign that 'AI that decides' is becoming its own category.

Source: [Google Blog ↗](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

---
## Under the Hood

### Shrinking AI search indexes with token pooling

**What happened**
Multi-vector embedding models power a precise kind of AI search: each word in your query gets its own chance to match something in a document. The catch is storage — a collection of millions of documents can mean hundreds of millions of stored vectors. Hugging Face describes training these models to expect 'token pooling', which merges similar vectors to cut that number down.

**Why it matters**
Training with pooling in mind means you can shrink the index without losing as much search quality, making high-accuracy semantic search cheaper to run at scale. Relevant to anyone building search or retrieval (RAG) systems.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/token-pooling)

### GitHub's guide to 'agentic engineering'

**What happened**
GitHub published a guide arguing that while writing code got faster with AI, the work around it — planning, reviewing changes, investigating production issues — didn't. It walks through using Copilot across each of those stages, and flags which parts still need human judgment.

**Why it matters**
A practical look at where AI coding agents fit into a full development workflow beyond autocomplete, useful for teams deciding how far to delegate to agents.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/)

---
**Fun fact:** A 2019 joke research paper found that 93% of paint splatters are valid Perl programs.

*Daily tech digest for curious professionals. AI news that affects your work.*