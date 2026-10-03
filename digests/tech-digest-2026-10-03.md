# Daily Tech Digest — Saturday, October 3 2026

> An AI has beaten the best human player of Stratego, a board game built on bluffing and hidden information, and it reportedly did it on a modest budget.

---
## AI beats the best Stratego player in history — on a budget

**What happened**
Ars Technica reports that an AI system has beaten the strongest Stratego player on record. Stratego had long resisted AI because most of the information is hidden: you can't see which of your opponent's pieces is which, so the game rewards bluffing and reading intent rather than pure calculation.

**What this means**
Chess and Go were games where everything sits on the board; real work rarely is. Progress on games with hidden information and deception is a step towards AI that can handle negotiation, planning and decisions under uncertainty — and the fact it was done cheaply means these methods won't stay limited to the largest labs.

Source: [Ars Technica ↗](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)

---
## Quick Hits

### GitHub names three skills to strengthen as AI changes the job

GitHub published advice for developers whose work is being reshaped by AI: learn to direct AI agents, review what they produce with a critical eye, and keep your own judgment at the centre of the work. The advice travels well beyond software — if you hand drafts, research or analysis to AI, the same three habits apply to you.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/ai-is-rewriting-the-developer-career-ladder-heres-how-to-stand-out/)

### Court sides with EFF: Utah's VPN law asks for the impossible

A court agreed with the Electronic Frontier Foundation that Utah's law on VPNs — tools that hide where your internet connection comes from — demands something that can't technically be done. It's a reminder that tech laws can fail on how the technology actually works, which matters for anyone in legal or compliance roles tracking new state rules.

Source: [EFF ↗](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility)

### Black Forest Labs releases FLUX 3 Image

Black Forest Labs, the company behind the FLUX family of image generators, has published FLUX 3 Image, its new image model. If you're a designer or marketer who uses AI image tools, it's worth a look as another option alongside the big-name generators.

Source: [Black Forest Labs ↗](https://bfl.ai/models/flux-3-image)

### ChatGPT gets a "Sites" feature

OpenAI has a new feature page for Sites in ChatGPT, which drew wide attention on Hacker News today. Check the page for details if you've been looking for ways to turn your ChatGPT work into something you can share.

Source: [OpenAI ↗](https://chatgpt.com/features/sites/)

---
## Under the Hood

### AstaBrief: an open model for writing research reports with sources

**What happened**
The Allen Institute for AI open-sourced AstaBrief, the fast report-generation model inside its Asta research assistant. Their write-up covers how it was trained: first on example reports (supervised fine-tuning), then on pairs of better and worse answers (DPO), with extra data filtering aimed at getting attribution — which source supports which claim — right.

**Why it matters**
Reports that cite the wrong source are a common failure of AI research tools. An open model trained specifically for attribution, with the model and data released, gives researchers and builders something they can inspect and improve rather than trust blindly.

Source: [Hugging Face Blog (Ai2) ↗](https://huggingface.co/blog/allenai/astabrief)

### AutoSynthData: making practice tasks for workplace AI agents

**What happened**
ServiceNow described AutoSynthData, a system that generates training tasks for AI agents working inside enterprise software. Each task pairs a description of the system, a task for the agent, and a verifier that checks whether it was done correctly; tasks are built from the model's own failures and checked and repaired both one by one and in batches.

**Why it matters**
Agents that work inside business software are hard to train because real practice data is scarce and sensitive. Generating verified synthetic tasks is one way companies are trying to make agents reliable without exposing customer data.

Source: [Hugging Face Blog (ServiceNow) ↗](https://huggingface.co/blog/ServiceNow-AI/autosynthdata)

---
**Fun fact:** The first data packet ever sent by carrier pigeon, under a joke internet standard, is now up for auction at Christie's.

*Daily tech digest for curious professionals. AI news that affects your work.*