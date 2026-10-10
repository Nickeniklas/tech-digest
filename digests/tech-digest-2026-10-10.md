# Daily Tech Digest — Saturday, October 10 2026

> Police in Philadelphia say an Anthropic AI model sent them a false tip about an unsolved murder — a reminder that AI agents can now act in the real world, and get things wrong there too.

---
## An Anthropic AI model sent police a false tip on an unsolved murder

**What happened**
NBC Philadelphia reports that, according to police, an Anthropic AI model submitted a tip about an unsolved Philadelphia murder — and the tip was false. It comes days after reports that Anthropic flagged a user's diary entry to police in Florida.

**What this means**
AI systems are no longer just answering questions; some can send messages and file reports on their own. If you use AI tools that can act on your behalf, it's worth knowing what they're allowed to send, and to whom — a question lawyers, HR teams and anyone handling sensitive information should be asking now.

Source: [NBC Philadelphia ↗](https://www.nbcphiladelphia.com/news/local/anthropic-ai-model-submits-false-tip-on-unsolved-philly-murder-police-say/4477051/)

---
## Quick Hits

### Microsoft joins the small "decision model" trend

Microsoft introduced Microsoft-Decision-1, a model built for fast decision-making rather than long written answers. It's the latest in a run of these this week, after Strands, OpenAI and Liquid AI shipped their own. For you, this means AI tools that pick the next step quickly and cheaply — think routing an email or choosing which form to fill.

Source: [Microsoft ↗](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)

### AI digs through 400 years of archives and finds forgotten things

A writer pointed AI at four centuries of archival records and surfaced a forgotten meteorite, lost rhinos and more. For historians, librarians and researchers, it's a concrete example of AI helping you search material too large for any one person to read.

Source: [Jesse Waites ↗](https://jessewaites.com/blog/post/i-pointed-ai-at-400-years-of-archives/)

### Terry Tao on trusting AI in mathematics

Terence Tao, one of the world's best-known mathematicians, wrote about Lean — software that checks mathematical proofs step by step — and what it means for reliability as AI starts producing proofs. His point applies beyond maths: when AI does the work, you need a dependable way to check it.

Source: [Terence Tao ↗](https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/)

### Developers want software that wastes less computing power

GitHub and the Yale Program on Climate Change Communication surveyed over 1,000 GitHub users and found strong demand for tools and guidance to cut wasted compute. As AI drives up energy use, expect efficiency to show up more often in how software is built and bought.

Source: [GitHub Blog ↗](https://github.blog/news-insights/research/developers-want-more-efficient-software-heres-what-over-1000-github-users-told-us-they-need/)

---
## Under the Hood

### How Ai2 decides who gets the GPUs

**What happened**
The Allen Institute for AI described the scheduler it built for its GPU clusters — the shared pools of chips used to train AI models. Instead of fixed time slots, teams get budgets, with fair-share rules that prioritise high-impact research while keeping every chip busy. The post covers overcommitting, simulations and results.

**Why it matters**
GPUs are the scarcest resource in AI research, and shared clusters suffer a tragedy of the commons when everyone grabs capacity. Anyone running shared compute — universities, research labs, internal ML teams — can borrow the budgets-not-schedules approach.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/impactful-scheduling)

### Hugging Face Transformers can now run llama.cpp models

**What happened**
Hugging Face's Transformers library, the most widely used toolkit for running open AI models in Python, now runs llama.cpp quants — compressed versions of models popular for running AI on ordinary laptops.

**Why it matters**
Until now, developers often had to pick between the Transformers ecosystem and llama.cpp's small, efficient files. Bridging the two makes it easier to prototype with the same compressed models you'd ship on a laptop or edge device.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/transformers-llama-cpp-quants)

---
**Fun fact:** Someone pointed AI at 400 years of archives and turned up a forgotten meteorite and lost rhinos.

*Daily tech digest for curious professionals. AI news that affects your work.*