# Daily Tech Digest — Monday, October 5 2026

> A badly blacked-out document has handed the public a rare look at how much water and electricity a Google data center actually uses.

---
## A redaction mistake reveals a Google data center's water and power use

**What happened**
Local outlet 1011 Now reports that an improperly redacted document exposed water and electricity figures for Google's data center in Lincoln, Nebraska — numbers that were meant to stay hidden. The story drew wide attention on Hacker News today.

**What this means**
The resources AI data centers consume are usually kept confidential, so leaks like this are one of the few ways communities learn the real costs. If you work in local government, planning, journalism or sustainability, expect more pressure for these figures to be disclosed on purpose.

Source: [1011 Now ↗](https://www.1011now.com/2026/09/30/more-questions-than-answers-about-lincolns-google-data-center-water-electricity-usage/)

---
## Quick Hits

### UK safety institute works to make AI test scores repeatable

The UK's AI Security Institute and the EvalEval group described how they are making AI benchmark results reproducible, so a score one lab reports can be checked by someone else. When companies advertise how well their models perform, this is what lets you trust the number.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/evaleval-aisi)

### GitHub Universe 2026: checking AI-written code takes centre stage

GitHub previewed ten talks from its upcoming Universe conference, with sessions on verifying code written by AI and on keeping software building blocks secure. It's a sign that the conversation has shifted from what AI can produce to how you check it.

Source: [GitHub Blog ↗](https://github.blog/news-insights/company-news/10-technical-talks-im-excited-about-at-github-universe-2026/)

### A free tool turns off Apple Intelligence on Macs and reclaims the space

An open-source project shows how to switch off Apple Intelligence on macOS 27 and recover the disk space its AI models take up. If your Mac is short on storage and you don't use Apple's AI features, this is the trade-off people are weighing.

Source: [GitHub ↗](https://github.com/omlahore/RemoveMacAI)

### A software glitch leaves F1 drivers without power in Bahrain

Formula 1 drivers were left frustrated over a software glitch in Bahrain that left them powerless, Motorsport.com reports, with the problem described as "totally unacceptable". It's a reminder of how much modern machines — even race cars — depend on code working perfectly.

Source: [Motorsport.com ↗](https://www.motorsport.com/f1/news/horrible-totally-unacceptable-powerless-f1-drivers-frustrated-by-bahrain-f1-software-glitch/10861968/)

---
## Under the Hood

### A 125-billion-parameter model running on a single gaming graphics card

**What happened**
A project called Strata claims to run Qwen 3.8 Flash Next — a 125-billion-parameter open model — on one consumer RTX 4090 graphics card at about 100 tokens (word pieces) per second. Models this size normally need data-center hardware with far more memory than the 4090's 24 GB.

**Why it matters**
If the numbers hold up, large open models become usable on a single desktop PC, which matters for anyone who wants to keep data on their own machine instead of sending it to a cloud service. Treat it as a claim to verify: it's a fresh hobby project, not an independent benchmark.

Source: [GitHub ↗](https://github.com/Niko1221/Strata)

### Your AI agent passed once. Will it pass again?

**What happened**
IBM Research wrote on the Hugging Face blog about measuring whether an AI agent succeeds consistently on the same task, not just once. Agents built on large language models can give different results on repeated runs, so a single successful demo says little about day-to-day reliability.

**Why it matters**
For teams putting agents into real workflows, consistency is the number that decides whether you can hand off a task without checking every result. It builds on a growing push — including Microsoft's ThinkingBox work covered yesterday — to test agents on outcomes rather than single runs.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/ibm-research/altk-evolve-consistency)

---
**Fun fact:** One Hacker News favourite today: a working pendulum clock, built entirely from trash, that runs for 30 minutes.

*Daily tech digest for curious professionals. AI news that affects your work.*