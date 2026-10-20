# Daily Tech Digest — Tuesday, October 20 2026

> WhatsApp's help pages were found to contain hidden instructions telling AI assistants not to point you to a regulator — a reminder that the AI answers you get can be shaped by text you never see.

---
## WhatsApp's help pages hid instructions aimed at AI assistants

**What happened**
Privacy company Redact reports that WhatsApp's help pages contained hidden text written for AI chatbots, instructing them not to recommend contacting a regulator. Human visitors wouldn't see it, but an AI assistant reading the page to answer your question would.

**What this means**
When you ask an AI tool to summarise a company's policies, the answer can be steered by instructions buried in the pages it reads. If you handle complaints, compliance or consumer rights — lawyers, HR and customer-facing teams especially — check the original source before relying on an AI summary of what your options are.

Source: [Redact ↗](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions)

---
## Quick Hits

### MiniMax releases M3.1 Flash

Chinese AI company MiniMax published M3.1 Flash, a new model in its lineup. "Flash" versions are usually built to be faster and cheaper to run than a company's flagship model, which is what makes them practical for everyday tools.

Source: [MiniMax ↗](https://www.minimax.io/blog/minimax-m31f)

### France's supermarket fridges were exposed online for months

Previously covered on 2026-10-13: hackers remotely defrosted supermarket fridges across Europe. Since then, IPinfo reports that French supermarket refrigeration systems were reachable on the open internet for months before the attack. It's a familiar lesson: connected equipment left exposed eventually gets found.

Source: [IPinfo ↗](https://ipinfo.io/blog/france-fridges-hack)

### Move a Copilot app session into VS Code without starting over

GitHub explains how to hand off a session from its Copilot app to the VS Code editor while keeping the conversation, code changes and working context. You can start a task in one place and finish it in another without re-explaining what you were doing.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/)

### RuneScape Bench tests AI agents inside an online game

RuneScape Bench uses the long-running online game RuneScape as a testing ground for AI agents — programs that act on their own toward a goal. Games like this require planning, trading and many small steps over time, which is closer to real work than a quiz-style test.

Source: [YouTube ↗](https://www.youtube.com/watch?v=cNm4zyUtWj0)

---
## Under the Hood

### How "abliterated" models can get you hacked

**What happened**
Security firm ProjectDiscovery published research on the risks of abliterated models — open AI models that have been modified to remove their built-in refusals, so they'll answer anything. These modified copies circulate freely and are popular with people who find standard models too restrictive.

**Why it matters**
Downloading a modified model from an unknown source is a lot like running unknown software: you are trusting whoever changed it. For teams experimenting with self-hosted models, it's a case for sticking to official releases and treating community variants as untrusted.

Source: [ProjectDiscovery ↗](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned)

### TorchNeuron: Hugging Face models now run natively on AWS Trainium

**What happened**
Hugging Face introduced TorchNeuron, a new native backend for PyTorch on AWS Trainium, Amazon's own AI chips. Its Transformers, Diffusers and Kernels libraries now support it directly, so models can run on Trainium without a separate conversion step.

**Why it matters**
Most AI work today runs on NVIDIA hardware. Making Amazon's chips a first-class option in the most widely used open-model libraries gives teams another place to run models, which can mean more choice on price and availability.

Source: [HuggingFace Blog ↗](https://huggingface.co/blog/hf-torchneuron)

---
**Fun fact:** Ukraine says it has carried out its first evacuation of a wounded soldier from the front line by drone.

*Daily tech digest for curious professionals. AI news that affects your work.*