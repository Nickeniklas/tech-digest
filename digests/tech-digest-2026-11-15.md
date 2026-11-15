# Daily Tech Digest — Sunday, November 15 2026

> Apps built in minutes with an AI app builder have been leaking passport details and private messages — a reminder that 'easy to build' doesn't mean 'safe to launch'.

---
## Apps made with AI builder Lovable exposed passport details and 200,000+ private messages

**What happened**
Security researchers report that apps created with Lovable — a popular tool that lets you build a working app by describing it in plain words — left users' passport details and more than 200,000 private messages open to anyone who knew where to look.

**What this means**
AI app builders let non-developers ship real products fast, but they don't automatically lock down the data those apps collect. If your team has launched a tool this way — a client portal, a sign-up form, an internal app — have someone check who can actually see the data behind it before you collect anything sensitive.

Source: [Crissy Field Research ↗](https://www.crissyfield.de/research/lovable-en/)

---
## Quick Hits

### AI uses more energy when you write in languages other than English

University of Michigan researchers report that generative AI consumes more energy to handle non-English text than English. If you work in another language, the same request can cost more to run — a hidden unfairness in how these tools are built and priced.

Source: [University of Michigan ↗](https://news.umich.edu/generative-ai-uses-more-energy-on-non-english-text/)

### LinkedIn and Monster remove 1,000+ fake job postings

After an investigation by Canadian broadcaster CBC, LinkedIn and Monster took down more than 1,000 fake job ads. If you're hiring or job hunting, it's a reminder that a listing on a big platform isn't proof it's real — check the company directly before sharing personal details.

Source: [CBC News ↗](https://www.cbc.ca/news/canada/linkedin-monster-take-down-over-1-000-fake-job-postings-after-cbc-investigation-9.7415379)

### Digital-rights group asks court to require warrants for license-plate camera searches

The Electronic Frontier Foundation is asking a US appeals court to rule that police need a warrant before searching data from automated license plate readers — cameras that log where cars go. The outcome could shape how much of your daily movement can be looked up without a judge's sign-off.

Source: [EFF ↗](https://www.eff.org/deeplinks/2026/11/were-asking-appeals-court-require-warrant-alpr-searches)

### The US flight halt came down to one router in Arkansas

Previously covered on 2026-11-14: the FAA stopped departing flights nationwide for about 4.5 hours. Since then, the Wall Street Journal has traced the shutdown to a single router in southern Arkansas — a stark example of how one weak point can ground a whole system.

Source: [The Wall Street Journal ↗](https://www.wsj.com/business/airlines/the-single-router-in-southern-arkansas-that-ground-air-travel-to-a-halt-eedc326c)

---
## Under the Hood

### Google Project Zero will disclose bugs 90 days after reporting them

**What happened**
Google's Project Zero, its team that hunts security flaws in other companies' software, says it will make vulnerabilities public 90 days after reporting them to the vendor. A fixed public deadline puts pressure on software makers to ship fixes rather than sit on them.

**Why it matters**
For IT and security teams, a predictable 90-day clock means patches for Project Zero findings should land within that window — and that unpatched details may become public once it passes. Worth factoring into how quickly you apply vendor updates.

Source: [Google Project Zero ↗](https://projectzero.google/2026/11/disclosure-policy.html)

### DeepSeek V3 rebuilt in about 200 lines of code

**What happened**
A developer has published a compact version of DeepSeek V3, a large open AI model, written in roughly 200 lines of pure JAX — Google's library for numerical computing. Big models are usually spread across thousands of lines of code; a version this short is meant to be read end to end.

**Why it matters**
It's a learning resource: students and engineers can see the core design of a modern large model in one sitting, without wading through production code. It's for understanding the architecture, not for running the full-size model.

Source: [GitHub (Show HN) ↗](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax)

---
**Fun fact:** The nationwide US flight halt covered here yesterday has been traced to a single router in southern Arkansas.

*Daily tech digest for curious professionals. AI news that affects your work.*