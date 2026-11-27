# Daily Tech Digest — Friday, November 27 2026

> Google is setting the rules for how AI assistants reach your Gmail and Docs, and Anthropic shows AI helping track an Ebola outbreak.

---
## The Situation Report: Anthropic on AI in an Ebola response

**What happened**
Anthropic published a feature on the Ebola response in Butembo, in the eastern Democratic Republic of the Congo, where community health workers text daily notes on fevers, recoveries and deaths over WhatsApp. Those scattered counts become the situation reports responders rely on to decide where to act.

**What this means**
This is AI applied to a messy, everyday problem: turning informal notes into data people can act on. If your work involves pulling reports together from emails, chats or spreadsheets — in healthcare, NGOs, operations or local government — it shows where these tools can actually save time.

Source: [Anthropic ↗](https://www.anthropic.com/features/ebola-response)

---
## Quick Hits

### Google will route AI agents through its own Workspace connectors — and the Gmail one can't send email

Google plans to make AI agents use its own MCP servers, the official connectors that let AI tools reach Gmail, Docs and other Workspace apps. According to a widely shared write-up, the Gmail connector can't send email. If you hoped an AI assistant would handle your inbox end to end, expect it to draft rather than send for now.

Source: [Tech Stackups ↗](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

### Google Play will show solo developers' phone numbers and addresses

Google says it will display the phone numbers and addresses of Android developers who publish apps as individuals. For freelancers and one-person studios, that can mean a home address on a public app page — worth checking before you publish an app under your own name.

Source: [Google Play Console Help ↗](https://support.google.com/googleplay/android-developer/answer/17594752?hl=en)

### Hugging Face and OpenRouter team up on open models

Hugging Face, the largest hub for open AI models, is partnering with OpenRouter, a service that gives you one account for many AI providers. The goal is to make open-weight models — ones anyone can download and run — as easy to use as the big commercial chatbots.

Source: [Hugging Face ↗](https://huggingface.co/blog/openrouter)

### AI agents now manage part of DeepMind's computing power

The Decoder reports that AI agents now control part of the computing resources Google DeepMind uses for Gemini experiments. The same report notes that AI improving itself without human help remains a distant prospect.

Source: [The Decoder ↗](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)

---
## Under the Hood

### A benchmark dashboard for running AI locally on AMD hardware

**What happened**
The llama.cpp team launched a benchmark dashboard on Hugging Face that tracks how fast AI models run on AMD Ryzen processors and Radeon graphics cards. It covers prompt processing and text generation speed across llama.cpp builds, models and quantizations (compressed model versions). Separately, a developer published an AMD-specific fork of llama.cpp.

**Why it matters**
Local AI has mostly meant NVIDIA hardware. Public, per-build numbers make it easier to judge whether an AMD laptop or desktop is fast enough before you buy one or roll it out to a team.

Source: [Hugging Face ↗](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench)

### NVIDIA opens up data and fine-tuning for its document-reading model

**What happened**
NVIDIA followed up on Nemotron 3.5 Parse, a compact model that turns images of document pages into structured data, with open training data, fine-tuning guidance and faster inference (running the model).

**Why it matters**
Reading PDFs and scans reliably is the first step for AI search over company documents. Open data and fine-tuning let teams adapt the model to their own forms, invoices or contracts.

Source: [Hugging Face ↗](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)

---
**Fun fact:** Europe's top astronomy body just issued a statement on approving the launch of one million data centres into space.

*Daily tech digest for curious professionals. AI news that affects your work.*