# Daily Tech Digest — Tuesday, October 6 2026

> ChatGPT is putting real cartoonists' signatures on cartoons it made up, which raises a hard question about who gets credit for AI-made work.

---
## ChatGPT is signing fake New Yorker cartoons with real cartoonists' names

**What happened**
Nieman Lab reports that when people ask ChatGPT for cartoons in the style of The New Yorker, it sometimes adds the signatures of real, working cartoonists to images those artists never drew.

**What this means**
A signature tells readers who made something, so a forged one can mislead people and hurt an artist's reputation. If you're a designer, marketer, or editor using AI images, check every generated picture for names, logos, or signatures before you publish it. Lawyers will want to follow how publishers and artists respond.

Source: [Nieman Lab ↗](https://www.niemanlab.org/2026/10/chatgpt-is-adding-real-cartoonists-signatures-to-fake-new-yorker-cartoons/)

---
## Quick Hits

### Reflection releases Beam, a 501-billion-parameter open model

Reflection has released Beam, an open-weight AI model with 501 billion parameters. Open-weight means anyone can download the model and run it on their own servers. That gives organisations with strict data rules another large model they can keep entirely in-house.

Source: [Reflection ↗](https://reflection.ai/blog/introducing-beam)

### A two-year school study puts AI tutor Khanmigo to the test

A new working paper reports on a two-year experiment that used Khanmigo, Khan Academy's AI tutor, in schools. Most claims about AI tutoring come from short pilots, so evidence gathered over two school years is rarer. Teachers and school leaders weighing AI tutors should look at the full results.

Source: [EdWorkingPapers ↗](https://edworkingpapers.com/ai26-1551)

### Anthropic reported a user's diary entry to police

TechSpot reports that a Florida woman who used Claude as a diary now faces a felony charge after Anthropic reported one of her entries to police. The case is a reminder that what you write to an AI chatbot is not private the way a paper diary is. Read your provider's policy on when it shares conversations with authorities.

Source: [TechSpot ↗](https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html)

### AI agents propose two new materials for faster electronics

Vals AI says AI agents built on Claude Opus 5.5 found two candidate materials that could act as magnetic semiconductors at room temperature. Materials like these could lead to electronics that store and process information more efficiently. They are only candidates for now, and lab tests still have to confirm them.

Source: [Vals AI ↗](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)

---
## Under the Hood

### ReviewBench: an open benchmark for AI code reviewers

**What happened**
GitHub launched ReviewBench, a public benchmark for AI agents that review code. It is built from representative GitHub pull requests (proposed code changes), checks answers against expected findings drawn from several sources, and scores agents with metrics designed to match how code review works in practice.

**Why it matters**
More and more code is reviewed by AI before a person sees it. An open, shared test lets teams compare AI reviewers on realistic changes instead of trusting vendor claims, and makes it easier to see which tools actually catch problems.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/)

### Dust: training AI models without backpropagation

**What happened**
Qlabs published Dust, research on pretraining transformer models (the design behind most chatbots) without backpropagation. Backpropagation is the standard way neural networks learn: the model makes a guess, measures its error, and passes corrections backwards through every layer.

**Why it matters**
Almost every large AI model today learns through backpropagation, and that process drives much of the memory use and hardware cost of training. A workable alternative could change how and where models get trained. For now this is a research result, not a replacement for current methods.

Source: [Qlabs ↗](https://qlabs.sh/research/dust)

---
**Fun fact:** AI agents running Claude Opus 5.5 turned up two candidate materials for room-temperature magnetic semiconductors.

*Daily tech digest for curious professionals. AI news that affects your work.*