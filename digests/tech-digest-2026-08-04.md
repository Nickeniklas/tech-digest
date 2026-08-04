# Daily Tech Digest — Tuesday, August 4 2026

> OpenAI says its models helped produce ten new results in mathematics — and separately, an 80-billion-parameter AI now runs on a laptop.

---
## OpenAI Publishes Ten New Results in Mathematics and Computer Science

**What happened**
OpenAI published a list of ten advances in mathematics and theoretical computer science that its models contributed to. These are the kinds of problems where an answer is either provably right or wrong, so the contributions can be checked rather than taken on trust.

**What this means**
Most AI claims are hard to verify, which is exactly why this one is worth noting — mathematics is one of the few fields where you can prove the machine was correct. If you work in law, finance, or research, expect the argument to shift from whether AI can produce novel work to which fields let you check that it did.

Source: [OpenAI ↗](https://openai.com/index/ten-advances-in-mathematics/)

---
## Quick Hits

### A Large AI Model Now Fits on a Laptop — and a Smaller One on Your Phone

A developer released Swiftlet, an open-source tool that runs Qwen, an 80-billion-parameter AI model, in 4.3 GB of memory on a Mac, and a 35-billion-parameter model on an iPhone. Models that size normally need a server rack. If this holds up, the practical case for sending your documents to someone else's cloud gets weaker every month.

Source: [GitHub ↗](https://github.com/leonickson1/Swiftlet)

### AI Helps Experts More Than It Helps Beginners

Engineer Sean Goedecke argues that large language models pay off in proportion to what you already know: an expert spots the wrong answer and redirects, while a novice takes it at face value. The tool amplifies judgement rather than replacing it. It's a useful counterweight to the assumption that AI flattens the gap between newcomers and veterans.

Source: [Sean Goedecke ↗](https://www.seangoedecke.com/llms-reward-expertise/)

### A New Video Model Arrives With Sound Built In

MiniMax released H3, a video generation model with openly published weights, native audio, and output up to 2K resolution — and it works in ComfyUI, a popular free tool for building image and video pipelines, from day one. Most video models still generate silent clips you have to score separately. For anyone producing marketing or training video, generating picture and sound together removes a whole step.

Source: [ComfyUI Blog ↗](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)

### A Benchmark for Whether Voice AI Actually Sounds Human

Hugging Face published Real World VoiceEQ, a way of measuring the human quality of voice AI rather than just its accuracy. Existing tests check whether a system heard the words correctly, not whether talking to it is bearable. If your organisation is weighing up a voice assistant for customer calls, this is the gap between a system that passes a demo and one your customers will tolerate.

Source: [Hugging Face ↗](https://huggingface.co/blog/real-world-voiceeq)

---
## Under the Hood

### Cloudflare on Serving Open Models at Scale

**What happened**
Cloudflare wrote up how it runs Kimi and GLM — two large open-weight models — across its network, covering the compression work that shrinks them, the changes that cut response time, and the guardrails around what they output.

**Why it matters**
Serving an open model is a different problem from training one, and it is the part most companies actually face. The constraints are memory per machine, latency per request, and what happens when a model returns something it shouldn't. Worth reading if you're evaluating self-hosting against an API.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/smaller-faster-safer-models/)

### Why Routing Between AI Models Is Harder Than It Looks

**What happened**
IBM Research published a piece on model routing — automatically sending each request to the cheapest model that can handle it, and escalating to a stronger one only when needed. The idea is straightforward; the difficulty is deciding, before you have the answer, which requests are hard.

**Why it matters**
Routing is the main lever for cutting AI costs without visibly degrading quality, and most teams building on multiple models end up implementing some version of it. The failure mode is subtle: a router that misjudges difficulty saves money on the requests where accuracy mattered most.

Source: [Hugging Face ↗](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt)

---
**Fun fact:** The Dunning-Kruger effect may be a statistical artefact rather than a real pattern in how people judge themselves.

*Daily tech digest for curious professionals. AI news that affects your work.*