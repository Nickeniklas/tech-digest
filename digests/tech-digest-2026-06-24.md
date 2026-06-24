# Daily Tech Digest — Wednesday, June 24 2026

> The most interesting story today isn't a flashy new model — it's a manager who handed the boring half of their job to AI and got better at the rest.

---
## A Tech Leader Automated 40 Parts of Their Own Job

**What happened**
A senior leader at GitHub wrote about how they now lean on roughly 40 small automations — built with AI and simple scripts — to handle routine parts of their day, from triaging messages to prepping reports and tracking follow-ups.

**What this means**
For managers and knowledge workers, the takeaway isn't to automate yourself out of a job — it's to hand off repetitive work so you can spend more time on judgment, people, and decisions. Increasingly these tools can be set up without writing code, which puts them within reach of non-technical professionals.

Source: [GitHub Blog ↗](https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/)

---
## Quick Hits

### A Phone Keyboard That Types Without Sending Your Words Away

FUTO released a new swipe-typing model for its privacy-focused phone keyboard, letting you glide a finger across letters to spell whole words. Unlike the keyboards built into most phones, FUTO's runs entirely on your device, so what you type isn't sent off to a company's servers.

Source: [FUTO ↗](https://swipe.futo.tech/)

### A New Way to Drill for Clean Energy: Vaporise the Rock

Quaise Energy says it drilled 100 meters into hard granite using beams of millimeter-wave energy that essentially vaporise rock, instead of a traditional grinding drill bit. The goal is to reach the deep, hot rock needed for geothermal power almost anywhere — a possible path to clean, always-on electricity.

Source: [ThinkGeoEnergy ↗](https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/)

### Meta Pauses an Employee-Tracking Program After a Leak

Meta has paused an internal program that tracked employee activity after some of the collected data leaked inside the company. It's a reminder that workplace-monitoring tools carry their own privacy and security risks: the more an employer logs about its staff, the more there is to spill.

Source: [Wired ↗](https://www.wired.com/story/meta-pauses-employee-tracking-program-following-internal-security-breach/)

### GitHub Pushes Back on a California AI Transparency Law

GitHub joined a coalition asking California to amend its new AI Transparency Act, arguing the current wording could unintentionally burden open-source software shared freely online. They want the law's disclosure rules aimed at commercial AI products rather than volunteer maintainers.

Source: [GitHub Blog ↗](https://github.blog/news-insights/policy-news-and-insights/github-joins-coalition-advocating-for-fixes-to-california-ai-transparency-act-to-protect-open-source/)

---
## Under the Hood

### ByteDance Open-Sources a Harness for Long-Running AI Agents

**What happened**
ByteDance released deer-flow, an open-source framework for building AI agents that work on long, multi-step tasks — researching, coding, and creating content over minutes or hours rather than a single reply. It bundles sandboxes, persistent memory, tool access, reusable skills, sub-agents, and a message gateway into one system.

**Why it matters**
Most chatbots forget everything between turns and can't safely run code. A harness like this is what turns a plain language model into something closer to a co-worker you can hand a goal and leave to pursue it — and it's the kind of architecture many 'AI agent' products are quietly built on.

Source: [ByteDance (GitHub) ↗](https://github.com/bytedance/deer-flow)

### How Copilot Squeezes More Out of Every Token

**What happened**
GitHub published a technical look at how Copilot decides what to feed the model and which model to use for a given request — trimming irrelevant context and routing simpler tasks to cheaper, faster models while reserving the heavyweight ones for genuinely hard problems.

**Why it matters**
As AI coding tools shift to usage-based pricing, how efficiently they spend each token shows up directly on your bill. The same context-trimming and model-routing ideas apply to any team building its own product on top of large language models.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/getting-more-from-each-token-how-copilot-improves-context-handling-and-model-routing/)

---
**Fun fact:** Spare a thought for the engineer who invented the red and green squiggles under your typos, remembered this week.

*Daily tech digest for curious professionals. AI news that affects your work.*