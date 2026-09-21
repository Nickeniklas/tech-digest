# Daily Tech Digest — Monday, September 21 2026

> A report says ChatGPT is now watching what you do on other websites — and today's other stories are about who gets to check AI's work.

---
## ChatGPT is reportedly collecting what you do on other websites

**What happened**
A report circulating today says ChatGPT has started gathering data about the sites you visit outside the chat window, through an advertising data collector. OpenAI has not published details of what is collected or how long it is kept.

**What this means**
If you paste client emails, draft contracts or campaign plans into ChatGPT, it is worth knowing that the account doing that may also carry a record of your browsing. For lawyers, HR staff and anyone handling confidential material, this is the moment to check what your organisation's AI policy actually permits.

Source: [Buchodi ↗](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

---
## Quick Hits

### Qwen released a new image model

Alibaba's Qwen team published Qwen Image 2.1, the latest version of its image generation model. It is the kind of release that tends to show up inside design and marketing tools within weeks rather than months.

Source: [Qwen ↗](https://qwen.ai/blog?id=qwen-image-2.1)

### Spain has ordered blocks on Archive.today

Spanish authorities ordered internet providers to block Archive.today and its mirror sites. Archive pages are how many people preserve a web page as proof that it said something on a given day — a habit that quietly underpins a lot of legal, journalistic and academic work.

Source: [Reclaim The Net ↗](https://reclaimthenet.org/spain-blocks-archive-today-and-mirrors)

### Terence Tao asks what human mathematicians are still for

One of the world's leading mathematicians wrote about what remains of his field's work now that machines can handle more of the proving. His answer is worth reading in any profession where the routine part of the job is the part being automated first.

Source: [Terence Tao ↗](https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/)

### Do you still need to read the code an AI wrote?

GitHub's podcast took on the question directly, alongside arguments about which AI techniques are already obsolete. The underlying question applies well beyond code: how much of the work do you check when a machine produced it, and how would you know if it were wrong?

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/should-you-read-the-code-is-rag-dead-and-did-skills-kill-mcp/)

---
## Under the Hood

### Training a model across rented cloud jobs, without the usual plumbing

**What happened**
Hugging Face documented running asynchronous GRPO — a reinforcement learning method — with LoRA adapters spread across separate Hugging Face Jobs. Instead of the usual high-speed NCCL links between GPUs, the setup uses a storage bucket and a proxy to pass work between three jobs: the vLLM replicas that generate answers, the trainer that learns from them, and the router that keeps them in sync.

**Why it matters**
It is a working example of training a model on machines that never talk to each other directly. That matters for anyone who wants to fine-tune without booking a single large cluster — the hardware can be ordinary, rented and scattered.

Source: [Hugging Face ↗](https://huggingface.co/blog/asyncgrpo-lora-hfjobs)

### Google published an open orchestrator for AI agents

**What happened**
Google released AX, an open agentic orchestrator — software whose job is to co-ordinate several AI agents working on the same task, deciding what runs when and how results are passed along.

**Why it matters**
Orchestration is where most multi-agent projects currently fail: individual agents work, and then fall over when they have to hand work to each other. An open implementation from Google gives teams something to build on instead of writing that layer themselves.

Source: [AX ↗](https://agentexecutor.io)

---
**Fun fact:** A fan project has rebuilt Resident Evil 4's GameCube code in C++, byte-for-byte identical to the original.

*Daily tech digest for curious professionals. AI news that affects your work.*