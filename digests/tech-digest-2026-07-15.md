# Daily Tech Digest — Wednesday, July 15 2026

> The AI boom is quietly showing up on your electricity bill — plus a capable AI model that now fits in your pocket.

---
## The AI Data-Center Boom Is Raising Your Electricity Bill

**What happened**
A Fortune analysis found that the rapid build-out of data centers — much of it to power AI — has pushed roughly $23 billion in higher electricity costs onto ordinary utility customers, as grids strain to keep up with demand.

**What this means**
The cost of the AI boom is no longer abstract: it is landing on household and business power bills, even for people who never use these tools. Anyone managing an office budget or a home may notice utility costs creeping up, and it is becoming a live political issue in states courting big data-center projects.

Source: [Fortune ↗](https://fortune.com/2026/07/14/data-centers-23-billion-electricity-bills/)

---
## Quick Hits

### A Capable AI Model That Runs Entirely on Your Phone

A team released Bonsai 27B, an AI model in the same size class as many cloud services that runs directly on a phone — no internet connection and nothing sent to a company's servers. Running locally means your data stays on your device, which matters for anyone handling confidential client or student information.

Source: [PrismML ↗](https://prismml.com/news/bonsai-27b)

### Microsoft Patches a Record 570 Security Flaws

Microsoft's monthly security update fixed 570 vulnerabilities at once — the most it has ever addressed in a single batch. If your work laptop or company runs Windows, this is a reminder to let those updates install rather than clicking 'remind me later' for the third time.

Source: [Krebs on Security ↗](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)

### A Flaw in Tailscale's Popular Networking Tool Allowed Root Access

Tailscale, a widely used tool that lets companies connect their computers securely, disclosed a bug in its SSH feature that could have let an attacker gain full control of a machine. A fix is available, and IT teams using it should update promptly.

Source: [Tailscale Security Bulletins ↗](https://tailscale.com/security-bulletins)

### AI Cracks 20 Long-Standing Math Problems at Once

Researchers pointed 20 copies of OpenAI's Codex, running in parallel, at a famous list of unsolved problems posed by mathematician Paul Erdős — and reported solutions to 20 of them. It is an early sign that AI, run at scale, can chip away at questions that stumped people for decades.

Source: [Starfleet Math ↗](https://www.starfleetmath.com/)

---
## Under the Hood

### Dependabot Adds a Cooldown Before Adopting New Package Versions

**What happened**
GitHub's Dependabot — the bot that automatically suggests updates to the third-party code libraries a project depends on — now waits a built-in 'cooldown' period before proposing a brand-new release, rather than pulling it in the moment it appears.

**Why it matters**
A common supply-chain attack works by publishing a malicious version of a popular library and hoping automated tools grab it instantly. A default waiting period gives the community time to spot a bad release before it spreads, making the safer choice the default for millions of projects.

Source: [GitHub Changelog ↗](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/)

### A Developer Trained an AI 'World Model' to Play Super Mario Bros.

**What happened**
A developer built LeMario, a JEPA-style world model trained on Super Mario Bros. Rather than memorising the game, this kind of model learns an internal picture of how the game world behaves — what happens next when Mario jumps or a block is hit — and uses that to plan its moves.

**Why it matters**
World models are one of the main bets for the next stage of AI: systems that understand cause and effect rather than just predicting the next word or pixel. Seeing one built solo on a classic game is a clear, hands-on window into a technique that big labs are pouring resources into for robotics and reasoning.

Source: [Benjamin Bai ↗](https://www.benjamin-bai.com/projects/lemario)

---
**Fun fact:** One developer just built a working AI world model that plays Super Mario Bros. from scratch.

*Daily tech digest for curious professionals. AI news that affects your work.*