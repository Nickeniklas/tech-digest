# Daily Tech Digest — Thursday, November 19 2026

> Google has a new AI model that early testers already compare to the best on the market, and a real audit trial suggests AI agents can out-question professional accountants.

---
## Google releases Gemini 4 Neon

**What happened**
Google has introduced Gemini 4 Neon, the newest model in its Gemini AI family, a week after it announced Gemini 4 Hydrogen. One early review, widely shared on Hacker News, says Neon looks like a match for Anthropic's top model, Claude Opus 5.5.

**What this means**
If those early impressions hold, you'll have another top-tier option in the AI tools you already use, and competition like this tends to bring prices down and features in faster. Treat early reviews as first impressions rather than settled verdicts.

Source: [Google Blog ↗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---
## Quick Hits

### AI agents asked better questions than KPMG accountants in an audit trial

European Business Magazine reports on an audit trial in which AI agents asked better questions than KPMG's human accountants. Asking the right questions is a core skill in auditing, so this matters to accountants, auditors, and anyone in a review-heavy job: AI is moving past number-crunching into the judgment side of the work.

Source: [European Business Magazine ↗](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

### Microsoft unveils seven new AI models at Ignite

At its Ignite 2026 conference, Microsoft announced seven new AI models, pitched on 'scalable price-performance': a range of sizes, so businesses can pay less for simpler tasks. If your workplace runs on Microsoft 365, expect these to appear in the tools you use.

Source: [Microsoft AI ↗](https://microsoft.ai/news/microsoft-ignite-2026/)

### Serious security flaws found in Nginx, a common web server

Security firm Wiz reports flaws in Nginx, the software that serves a large share of the world's websites, that could let attackers run their own code without logging in. This follows last week's Apache flaw; if your organisation runs its own websites, check with IT that patches are applied.

Source: [Wiz ↗](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)

### How AI helps turn field notes into Ebola situation reports

Anthropic published a feature on the Ebola response in the eastern Democratic Republic of the Congo, where health workers text their daily counts of fevers, recoveries, and deaths over WhatsApp. Those notes become the situation reports responders rely on, and the piece shows how AI can help turn messy field data into usable information.

Source: [Anthropic ↗](https://www.anthropic.com/features/ebola-response)

---
## Under the Hood

### DaisyRose-27B: a strong agent model trained on a small budget

**What happened**
RadixArk released DaisyRose-27B, its first model, built on Qwen3.8-27B and trained with reinforcement learning (learning by trial and reward) on long-running agent tasks with sessions up to 1 million tokens. It needed just 1,200 curated tasks, 18 days, and 144 H200 GPUs.

**Why it matters**
Post-training (the fine-tuning that happens after a model's initial training) is where much of an agent's skill comes from. Showing strong results from a small, carefully chosen task set suggests smaller labs can compete without frontier-scale budgets.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin)

### Running a 180-billion-parameter model on 32GB of RAM

**What happened**
Hugging Face shows how to run a 180-billion-parameter 'mixture of experts' model, one that switches on only a few specialist sub-networks for each word, on a machine with just 32GB of memory. It does this by streaming the experts in from storage only as they're needed, using the Transformers library.

**Why it matters**
Models this large normally need expensive server hardware. Expert streaming trades speed for memory, making very large open models usable on ordinary workstations for testing and private, offline work.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/moe-expert-streaming)

---
**Fun fact:** Cambridge Dictionary's Word of the Year for 2026 is simply 'human'.

*Daily tech digest for curious professionals. AI news that affects your work.*