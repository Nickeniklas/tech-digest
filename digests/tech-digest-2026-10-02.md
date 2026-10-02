# Daily Tech Digest — Friday, October 2 2026

> A historian used an AI model to help turn up a previously unknown eyewitness account of the dodo, a bird that vanished more than 300 years ago.

---
## AI helps a historian find a new eyewitness record of the dodo

**What happened**
A historian writes that they used Anthropic's Claude Opus 5.5 to help locate and work through old sources, leading to a newly identified eyewitness record of the dodo. The model did the slow digging; the historian checked and interpreted what it found.

**What this means**
AI is becoming a practical research assistant for archives, not just a writing tool. If you work with old documents, records, or large text collections — historians, librarians, lawyers, journalists — this is a sign of where your own searches could get faster, with your judgement still doing the final check.

Source: [Res Obscura ↗](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness)

---
## Quick Hits

### Researchers study what your connected car knows about you

A team at Northeastern University published "Automatic Transmission", a data-privacy study of connected vehicles. Modern cars collect and send data about where and how you drive, so it's worth knowing what your car shares before you sign the terms at the dealership.

Source: [Northeastern University ↗](https://automatictransmission.khoury.northeastern.edu/index.html)

### OpenAI and Synopsys team up on AI for chip design

OpenAI and Synopsys, a major maker of chip-design software, announced GPT-Synopsys, a model aimed at helping engineers design computer chips. Chip design is slow and expensive, so even modest speed-ups could affect how quickly new hardware reaches the market.

Source: [Synopsys ↗](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design)

### arXiv tightens how fast you can download papers

arXiv, the free library where most AI and science research papers appear first, updated its rate-limit policy, which caps how many requests one visitor can make. If you or your team use tools that pull papers automatically, check that they still work under the new rules.

Source: [arXiv Blog ↗](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)

### GitHub publishes new transparency data and a policy outlook

GitHub released its latest transparency figures alongside an update on US state-level policy that affects developers and open-source projects. It's a useful read if your organisation publishes code openly or follows tech regulation.

Source: [GitHub Blog ↗](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/)

---
## Under the Hood

### Olmo-core 3: open tools for training very large AI models

**What happened**
The Allen Institute for AI released Olmo-core 3, open-source training infrastructure built around mixture-of-experts (MoE) models — models that route each input to a few specialised sub-networks instead of using the whole model every time. The release covers scaling and optimising MoE training into the trillion-parameter range, with a tech report, code, and an interactive demo.

**Why it matters**
Most labs training models this large keep their training stacks private. An open, documented stack lets universities and smaller teams study and reproduce frontier-scale training, and it will power the next generation of fully open Olmo models.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/olmocore3)

### Cloudflare launches Clef: open decision models you can fine-tune

**What happened**
Cloudflare announced Clef, a set of open-weight "decision models" — models built to choose between actions rather than write long answers — along with a new platform for fine-tuning them using reinforcement learning, a method where a model improves by being rewarded for good outcomes.

**Why it matters**
Open weights mean teams can run and adapt these models themselves, and pairing them with a hosted fine-tuning service lowers the bar for building specialised AI agents without training from scratch.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/clef-decision-models/)

---
**Fun fact:** The dodo was first described by Dutch sailors in 1598 and was gone within about 70 years.

*Daily tech digest for curious professionals. AI news that affects your work.*