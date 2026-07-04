# Daily Tech Digest — Saturday, July 4 2026

> Voice assistants are about to answer in real time, an AI learns to prove math theorems, and GitHub finally clears a mountain of security alerts.

---
## Voice AI Is About to Feel Instant

**What happened**
Hugging Face and chipmaker Cerebras built a speech system, using Google's open Gemma 4 model, that listens and talks back in near real time instead of the usual awkward pause. The whole pipeline — hearing you, thinking, and replying — runs fast enough to feel like a normal conversation.

**What this means**
The lag has been the main reason talking to AI still feels clunky. Cutting it changes the experience for anyone who leans on voice: customer-service teams, doctors dictating notes, and drivers or people with limited mobility who can't easily type.

Source: [Hugging Face ↗](https://huggingface.co/blog/cerebras-gemma4-voice-ai)

---
## Quick Hits

### Mistral Releases an AI That Proves Math

French lab Mistral released Leanstral 1.5, a model built to generate formal mathematical proofs that a computer can automatically check for errors. The pitch is "proof abundance" — turning careful mathematical reasoning, long a slow and specialist craft, into something you can produce at scale.

Source: [Mistral ↗](https://mistral.ai/news/leanstral-1-5/)

### GitHub Cleared 20,000 Security Alerts — and Hit Zero

GitHub had piled up more than 20,000 unresolved "leaked secret" alerts — exposed passwords and keys — across 15,000 of its own code repositories. Over nine months it sorted the real dangers from the noise and drove the backlog to zero, then wrote up how. If a company that builds security tools let that much pile up, it's a fair bet yours has too.

Source: [GitHub Blog ↗](https://github.blog/security/application-security/how-github-used-secret-scanning-to-reach-inbox-zero/)

### Six Free Settings That Make Your Code Harder to Attack

GitHub published a plain checklist of six security settings any project owner can switch on this week at no cost. None of them make you unhackable, but together they close the easy doors that opportunistic attackers rely on. Useful reading for anyone who manages a shared code project, technical or not.

Source: [GitHub Blog ↗](https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/)

### A Popular Windows App Could Hand Over Full Control

A researcher showed that MSI Center, software preinstalled on many MSI-brand PCs, could be tricked into granting an attacker the highest level of control over the machine within seconds. It's a reminder that the bundled utilities from your hardware maker can be a weak point, not just the programs you chose to install.

Source: [mrbruh.com ↗](https://mrbruh.com/msicenter/)

---
## Under the Hood

### The Same AI Model, Much Cheaper Hardware

**What happened**
Engineers ran the open GLM5.2 language model on AMD's MI355X accelerator and reported 2,626 tokens per second per server node — at roughly half the cost of running it on Nvidia's newer Blackwell chips. Tokens are the fragments of text a model reads and writes, so throughput per node is a direct measure of how much work one server does.

**Why it matters**
Nvidia dominates AI hardware, which keeps prices high. Credible results showing a competitor delivering comparable speed for less money matter to anyone paying inference bills — and hint at cheaper AI services downstream.

Source: [wafer.ai ↗](https://www.wafer.ai/blog/glm52-amd)

### Tiny OCR Models That Read 50 Languages

**What happened**
PaddlePaddle released PP-OCRv6, a family of optical-character-recognition models — software that turns pictures of text into editable text — spanning 50 languages. The versions range from a 1.5-million-parameter model light enough for a phone to a 34.5-million-parameter model for higher accuracy.

**Why it matters**
OCR quietly powers scanning receipts, digitising documents, and reading signs in translation apps. Models small enough to run on a phone mean this can happen on-device, without uploading your documents to a server.

Source: [Hugging Face ↗](https://huggingface.co/blog/PaddlePaddle/pp-ocrv6)

---
**Fun fact:** Mistral named its new proof AI "Leanstral" — a nod to Lean, the language for computer-checked mathematics.

*Daily tech digest for curious professionals. AI news that affects your work.*