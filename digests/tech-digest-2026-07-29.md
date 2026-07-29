# Daily Tech Digest — Wednesday, July 29 2026

> Markets got nervous about AI this week, and the sell-off in chip stocks says more about expectations than about the technology itself.

---
## Chip Stocks Slide as Investors Get Nervous About AI

**What happened**
Shares in chipmakers fell across the United States and Asia as investors reassessed how much money AI will actually make in the near term. The companies selling the hardware behind AI have been among the biggest winners of the past two years, which makes them the first to fall when confidence wobbles.

**What this means**
Market moods shape budgets: when investors cool on AI, the pressure on companies to show a return from their AI spending gets sharper, and that reaches the tools and pilots you are being asked to use at work. Nothing about the technology changed this week — the expectations around it did.

Source: [BBC ↗](https://www.bbc.com/news/articles/cly8zng43npo)

---
## Quick Hits

### Andrew Ng Launches a Company Built Around One-to-One Teaching

Andrew Ng, one of the best-known figures in AI education, unveiled LearnVector, a company focused on building one-to-one learning experiences rather than the one-size-fits-all courses that dominate online education. The pitch is that AI can finally make personal tutoring affordable at scale. If you teach or train people, this is the shape the competition is taking.

Source: [LearnVector ↗](https://learnvector.ai/)

### Anthropic Used Claude to Find Weaknesses in Encryption

Anthropic published research on using Claude to discover flaws in cryptography — the maths that protects your bank transfers, messages, and passwords. Finding these weaknesses has traditionally required rare human expertise and years of patience. The same capability cuts both ways, which is why the work is being published rather than kept quiet.

Source: [Anthropic ↗](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

### GitHub Shuts Down Attack Routes Into the Software Everyone Uses

GitHub detailed months of changes to npm and GitHub Actions — the plumbing that pulls free code components into most modern software — aimed at breaking the techniques attackers use to slip malicious code into them. These attacks matter to you indirectly: they are how a compromise in an obscure component ends up inside the apps your company runs.

Source: [GitHub Blog ↗](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)

### Apple Retires Its iPhone Upgrade Program

Apple is replacing the iPhone Upgrade Program with a new scheme called Apple Upgrade. The old programme bundled a yearly phone swap with insurance into one monthly payment. If you or your company buy phones on that plan, the terms you signed up for are changing.

Source: [Apple ↗](https://www.apple.com/shop/iphone/iphone-upgrade-program)

---
## Under the Hood

### A Minute-by-Minute Account of the July AI Break-In

**What happened**
Previously covered on 2026-07-22: Hugging Face disclosed that attackers, aided by AI acting largely on its own, broke into part of its production systems. Since then, Hugging Face has published the full technical timeline — how the intrusion started, what the automated attacker did at each step, and where it was eventually caught.

**Why it matters**
Post-incident write-ups at this level of detail are rare, and this is one of the first covering an attack where the AI did much of the work rather than assisting a human. Security teams get a concrete pattern to build detection around instead of speculation about what agentic attacks might look like.

Source: [Hugging Face ↗](https://huggingface.co/blog/agent-intrusion-technical-timeline)

### New Encoder Models Read Long Documents Fast on an Ordinary CPU

**What happened**
Liquid AI released LFM2.5-Encoders, a pair of models built for encoding — turning text into the numerical form that search, classification, and retrieval systems work with. The design targets long inputs running on a normal processor, not a graphics card, and the release includes benchmark results and fine-tuning recipes.

**Why it matters**
Most retrieval and search pipelines quietly depend on an encoder running over every document. Doing that well without GPUs changes what a small team can host on its own hardware, and it removes a per-query cost that made document-scale search expensive to run in-house.

Source: [Hugging Face ↗](https://huggingface.co/blog/LiquidAI/lfm2-5-encoders)

---
**Fun fact:** Someone just ported Half-Life to Mac OS 9 — an operating system Apple retired in 2001.

*Daily tech digest for curious professionals. AI news that affects your work.*