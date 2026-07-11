# Daily Tech Digest — Saturday, July 11 2026

> An AI just cracked a maths problem that stumped experts for decades — and Apple is taking OpenAI to court.

---
## An AI Produces a Proof That Eluded Mathematicians for 40 Years

**What happened**
Previously covered on 2026-07-10: OpenAI released GPT-5.6. Since then, a high-end version called GPT-5.6 Sol Ultra has produced a full written proof of the Cycle Double Cover Conjecture, a graph-theory problem that had resisted mathematicians since the mid-1980s. The proof runs to dozens of pages and is now being checked by human experts.

**What this means**
For years AI has helped with maths by suggesting steps; producing a complete, checkable proof of a famous open problem is a different order of thing. The catch is verification — a proof only counts once specialists confirm every line, so the real test is happening now, not in the press release.

Source: [OpenAI (proof PDF) ↗](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf)

---
## Quick Hits

### Apple Sues OpenAI Over Alleged Trade-Secret Theft

Apple has filed a lawsuit accusing OpenAI of taking confidential information through former Apple employees who moved to the AI company. It is a rare open legal fight between two of the biggest names in tech, and a sign of how fiercely companies are now guarding their AI talent and know-how.

Source: [9to5Mac ↗](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/)

### SpaceX Wants 100,000 More Starlink Satellites

SpaceX has asked regulators for permission to launch roughly 100,000 additional Starlink satellites, which it says would multiply the network's total capacity about a hundredfold. If approved it would be a huge expansion of satellite internet, though it also sharpens long-running worries about crowding in orbit.

Source: [ZDNET ↗](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/)

### New York City Moves to Ban Sneaky Subscription Traps

New York City passed rules cracking down on "deceptive subscription practices" — the hard-to-cancel sign-ups and hidden auto-renewals that quietly drain money each month. For anyone who markets or sells subscriptions, it is another signal that "easy to join, hard to leave" is becoming a legal liability.

Source: [The Guardian ↗](https://www.theguardian.com/us-news/2026/jul/10/new-york-city-deceptive-subscriptions-ban)

### A 15-Year-Old Flaw Found in Every Linux Distribution

Researchers disclosed GhostLock, a memory-handling bug that has been present in essentially all Linux distributions for about 15 years. Linux runs most of the world's servers and cloud services, so a flaw this widespread is worth patching promptly once your provider or IT team ships a fix.

Source: [Nebusec Research ↗](https://nebusec.ai/research/ionstack-part-2/)

---
## Under the Hood

### Profiling PyTorch Attention, One Backend at a Time

**What happened**
Hugging Face published the third part of a series on measuring where time actually goes inside a running AI model. It walks through the different ways PyTorch can compute "attention" — the core operation in modern language models — from a naive version to the highly optimised Flash and cuDNN backends, and shows how to profile each to see which is fastest on your hardware.

**Why it matters**
If you build or fine-tune models, picking the right attention backend can be the difference between a training run that takes hours and one that takes days — without changing the model itself. The piece is a practical guide to finding that speed rather than guessing at it.

```python
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend

with sdpa_kernel(SDPBackend.FLASH_ATTENTION):
    out = torch.nn.functional.scaled_dot_product_attention(q, k, v)

# swap the backend to compare timings on your own GPU
```

Source: [Hugging Face ↗](https://huggingface.co/blog/torch-attention-profile)

### Why GitHub Made Its Copilot Code Reviewer Use Plain Unix Tools

**What happened**
GitHub explained that adding fancy custom tools to its Copilot code-review agent actually made the reviews worse and more expensive. The fix was to give the agent simple, shared Unix-style commands — the same grep-and-read moves a human uses to explore a codebase — and to focus it on the concrete evidence in each pull request.

**Why it matters**
It is a useful counterexample to the idea that more tooling always makes an AI agent smarter. Anchoring the agent to familiar, general-purpose tools reduced cost and improved results, a lesson for anyone building agents that have to navigate real systems.

Source: [The GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/)

---
**Fun fact:** The graph-theory puzzle GPT-5.6 just solved had gone unproven since 1985 — older than most of the researchers who chased it.

*Daily tech digest for curious professionals. AI news that affects your work.*