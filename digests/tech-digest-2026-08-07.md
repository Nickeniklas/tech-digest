# Daily Tech Digest — Friday, August 7 2026

> When people are asked to approve what an AI assistant wants to do, they wave through a third of the dangerous requests.

---
## People Approving AI Actions Miss One Dangerous Request in Three

**What happened**
A study across 40,000 simulated runs found that when people were shown what an AI agent wanted to do and asked to approve or deny it, they missed roughly one in three harmful commands. The permission prompt — the safety step meant to keep a human in charge — turned out to be far weaker than assumed.

**What this means**
If your work involves clicking "allow" on what an AI assistant proposes — a lawyer letting it touch a document store, a manager approving an automated email send — that click is doing less protective work than it feels like. The practical fix is narrowing what the tool can reach in the first place, rather than relying on catching the bad request in the moment.

Source: [ScaleX ↗](https://scalex.dev/blog/ai-agent-permissions-stats/)

---
## Quick Hits

### Meta Ordered to Pay $942 Million Over Harm to Children

A court ordered Meta to pay $942 million to address harm caused to children by its social media products. It is one of the largest financial penalties yet tied to how a platform's design affects young users, and it lands while regulators in several countries are drafting similar rules.

Source: [The Wall Street Journal ↗](https://www.wsj.com/tech/meta-ordered-to-pay-942-million-to-address-harm-to-kids-from-social-media-8ba5aab7)

### A Reporter Was Stalked Through a Child's Smartwatch

Wired documented how hackers took over a smartwatch marketed for children and used it to track a person's movements and listen in. The watches are sold as a safety product for parents, which is exactly what makes the flaw worth knowing about before buying one.

Source: [Wired ↗](https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/)

### OpenAI Opens Its Newer Model to Free ChatGPT Users

Previously covered on 2026-07-31: OpenAI released GPT-5.6, pitched on price rather than raw capability. Since then, the company has expanded access to the Luna version for people on the free tier and shipped improvements to Sol, the other variant. If you use ChatGPT without paying, the model answering you has changed.

Source: [OpenAI ↗](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)

### USB-C Cable Labels Are Not Worth Trusting

A writer tested a drawer of USB-C cables with a meter and found the printed claims about charging speed and data transfer frequently did not match reality. If a laptop charges slowly or a file transfer crawls, the cable is a likelier culprit than the device.

Source: [MakeUseOf ↗](https://www.makeuseof.com/i-stopped-trusting-usb-c-cable-labels-started-testing-with-meter-instead/)

---
## Under the Hood

### GitHub's Malware Warnings Now Reach Past npm

**What happened**
GitHub's Advisory Database — the list it uses to warn projects that a piece of third-party code they depend on is malicious — previously covered only npm, the JavaScript package registry. GitHub has now wired in OpenSSF's malicious-packages data so advisories cover other language ecosystems too, and it describes building the ingestion pipeline deliberately paranoid, since the input is by definition a feed of hostile software.

**Why it matters**
Dependency malware is currently the most productive way to attack software teams, and the warning only works if it exists for the ecosystem you actually use. Broadening the feed closes the gap for teams working outside JavaScript, who until now got the same automated dependency alerts with much thinner malware coverage behind them.

Source: [The GitHub Blog ↗](https://github.blog/security/supply-chain-security/how-we-took-malware-advisories-beyond-npm/)

### Writing Code Got Cheap. Owning It Didn't.

**What happened**
GitHub's engineering team published a framework for deciding which changes are genuinely cheap now that AI tools write much of the code. Their argument: the cost of producing a feature has dropped sharply, but the cost of maintaining it — reviewing it, debugging it years later, keeping it secure — has not moved at all.

**Why it matters**
It reframes a decision every team is making badly right now. When a prototype takes an afternoon instead of a fortnight, the instinct is to say yes to more things, but the long-term bill arrives in maintenance rather than in the initial build.

Source: [The GitHub Blog ↗](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)

---
**Fun fact:** Quake just got an official update — the game is 30 years old this year.

*Daily tech digest for curious professionals. AI news that affects your work.*