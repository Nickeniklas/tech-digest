# Daily Tech Digest — Monday, July 13 2026

> A quirk in how your browser does basic math can now quietly reveal which computer you're using — plus real numbers on switching AI models, and one of the internet's founders steps back.

---
## Your Browser's Math Can Now Reveal Which Computer You're Using

**What happened**
Researchers found that since Chrome's latest Chromium update, a basic built-in math function returns slightly different results depending on your operating system, letting a website tell whether you're on Windows, Mac, or Linux — without ever asking.

**What this means**
This is one more signal advertisers and trackers can stitch together into a 'fingerprint' that follows you around the web, even if you block cookies or browse privately. For anyone handling sensitive work — lawyers, journalists, HR — it's a reminder that everyday privacy tools have real limits.

Source: [Scrapfly ↗](https://scrapfly.dev/posts/browser-math-os-fingerprint/)

---
## Quick Hits

### A Real Team Moved to GPT-5.6 and Cut Its Costs by a Quarter

Previously covered on 2026-07-10: OpenAI released GPT-5.6. Since then, an engineering team published results from moving their live AI product onto it, reporting the app ran about 2.2 times faster and cost 27% less to operate than on their previous model. It's a concrete data point for anyone weighing whether upgrading AI tools is worth the switching effort.

Source: [Ploy ↗](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

### One of the Internet's Founders Is Retiring at Last

Vint Cerf, widely called a 'father of the internet' for co-designing the basic rules that let computers talk to each other, is stepping back after decades at Google and across the industry. His work in the 1970s is why email, the web, and nearly everything else online can move between different machines and networks at all.

Source: [TechCrunch ↗](https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/)

### Google Wants AI to Smooth Out Your Commute

Google Research described a project that uses AI to fine-tune the timing of traffic lights, aiming to cut the stop-and-go congestion that wastes fuel and time. It's being tested with cities around the world, and the appeal is that it works with the traffic lights already on the street rather than requiring new hardware.

Source: [Google Research ↗](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

---
## Under the Hood

### How GitHub Cleared More Than 20,000 Security Alerts

**What happened**
GitHub explained how it faced over 20,000 'secret scanning' alerts — automated warnings that a password or access key may have been accidentally saved into code — spread across 15,000 of its own repositories, and how it worked through every one to reach zero in nine months.

**Why it matters**
Leaked credentials are one of the most common ways attackers get in. The write-up reads as a playbook for any security team buried in alerts: separate genuine risks from noise, automate the cleanup, and give every project a clear owner responsible for fixing it.

Source: [GitHub Blog ↗](https://github.blog/security/application-security/how-github-used-secret-scanning-to-reach-inbox-zero/)

### A New Test for AI That Modernizes Old Java Code

**What happened**
IBM Research released ScarfBench, a benchmark that measures how well AI 'agents' can migrate large enterprise Java applications from one software framework to another — the kind of tedious, error-prone rewrite that big companies spend heavily on.

**Why it matters**
Framework migrations are exactly the unglamorous, large-scale work businesses hope AI can absorb. A shared, public benchmark lets teams compare tools on the same task instead of taking vendor claims on faith — a small but important step toward trusting AI with real production code.

Source: [Hugging Face / IBM Research ↗](https://huggingface.co/blog/ibm-research/scarfbench)

---
**Fun fact:** Vint Cerf helped write the internet's basic rules in the 1970s — before most people had ever touched a computer.

*Daily tech digest for curious professionals. AI news that affects your work.*