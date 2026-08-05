# Daily Tech Digest — Wednesday, August 5 2026

> GitHub's lawyers built their own workflow tools without writing code — and a browser privacy flaw is leaking the addresses iPhone users thought were hidden.

---
## GitHub's Legal Team Built Its Own Tools — Without Writing Code

**What happened**
GitHub published an account of how its own legal team used Copilot CLI, a command-line AI assistant, to build small tools that automate parts of their day-to-day work. Nobody on the team wrote a line of code themselves; they described what they wanted in plain English and the assistant produced it.

**What this means**
This is the clearest signal yet that building simple internal tools is no longer gated behind an engineering team. If you run a legal, marketing, or operations function and keep a spreadsheet or a repetitive process held together by hand, that is now something you can plausibly automate yourself.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-the-github-legal-team-used-copilot-cli-to-streamline-their-workflows/)

---
## Quick Hits

### A Browser Flaw Is Leaking the Addresses iCloud Private Relay Hides

Security researchers at Mysk found that WebKit, the engine behind Safari and every browser on iPhone, leaks your real IP address and the sites you look up, even when you are using a proxy or Apple's iCloud Private Relay. Those are the exact tools people turn on to keep their browsing private. Until Apple ships a fix, treat Private Relay as a speed bump rather than a guarantee.

Source: [Mysk ↗](https://mysk.blog/2026/08/04/webkit-proxy-icloud-private-relay-ip-leak/)

### Mistral Releases a Free Model for Spotting Harmful Content

The French AI company Mistral released Shieldstral, a small open model that reviews both text and images and flags content that breaks safety rules. It is free to download and run, which matters for organisations that cannot send user content to an outside service. Anyone running a community forum, a school platform, or a customer chat now has a moderation option that stays on their own servers.

Source: [Mistral ↗](https://mistral.ai/news/shieldstral/)

### Interpol Says AI Now Drives Most Cybercrime in Africa

Interpol reported that more than half of cybercrime across Africa is now powered by AI, as automated scams surge. The tooling that makes a convincing fake message cheap to produce is the same tooling that makes it cheap to produce a million of them. Expect the phishing attempts landing in your inbox to keep getting better written and harder to spot.

Source: [Africanews ↗](https://www.africanews.com/2026/08/04/ai-fuels-more-than-half-of-cybercrime-in-africa-as-digital-scams-surge-interpol/)

### Flowise, a Popular Drag-and-Drop AI Builder, Is Shutting Down

Flowise, one of the better-known tools for assembling AI workflows by dragging boxes around instead of coding, announced it is sunsetting. Teams that built internal chatbots or document assistants on it will need somewhere else to go. It is a useful reminder to check whether the AI tools your work depends on have a business behind them that will still exist next year.

Source: [Flowise ↗](https://flowiseai.com/sunset)

---
## Under the Hood

### An Active Supply Chain Attack Has Compromised Keyv and Its Neighbours

**What happened**
Security firm Aikido reported that Keyv — a widely used npm package for caching data, pulled in indirectly by a great many JavaScript projects — has been compromised as part of the ongoing Shai-Hulud campaign. The attack works by stealing a maintainer's publishing credentials, pushing a poisoned version of their package, and using it to harvest more credentials from whoever installs it, which then spreads to further packages.

**Why it matters**
This is the failure mode that keeps appearing: almost nobody installs Keyv deliberately, but thousands of projects inherit it three or four levels down their dependency tree. If you maintain a JavaScript codebase, pin your versions, audit your lockfile for recently published updates, and rotate any tokens that sat on a machine that ran an install this week.

```python
npm ls keyv
npm audit --production
npm install --ignore-scripts
```

Source: [Aikido Security ↗](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack)

### Liquid AI Ships a 2.6-Billion-Parameter Agent That Runs on the Device Itself

**What happened**
Previously covered on 2026-07-29: Liquid AI released the LFM2.5 encoder models, built to read long documents quickly on an ordinary CPU. Since then, the company has released LFM2.5-2.6B, a model small enough to run entirely on a phone or laptop that still supports tool calling and multi-step workflows — the things an AI agent needs in order to actually do a task rather than just answer a question.

**Why it matters**
On-device agents change what is possible in regulated settings. Nothing leaves the hardware, so there is no vendor to sign a data processing agreement with and no network round trip to wait for. The trade-off is capability: a 2.6-billion-parameter model is a fraction of the size of a frontier model, so it works best on narrow, well-defined jobs.

Source: [Hugging Face ↗](https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b)

---
**Fun fact:** The City of Munich is paying for a six-month sabbatical so one developer can maintain libexpat.

*Daily tech digest for curious professionals. AI news that affects your work.*