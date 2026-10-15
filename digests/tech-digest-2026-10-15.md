# Daily Tech Digest — Thursday, October 15 2026

> AI can now produce detailed, town-scale climate simulations for a tiny fraction of what supercomputers cost — including the rare extreme storms that matter most.

---
## AI simulates extreme weather at 3 km detail for a fraction of the cost

**What happened**
The Allen Institute for AI (Ai2) released HiRO-ACEv2, an AI climate emulator — a model that imitates expensive physics-based climate simulations. It can reproduce even very rare rain, wind and pressure extremes with high accuracy, and the full system generates global climate data at 3 km resolution for about 1/300th of the cost of a comparable traditional simulation.

**What this means**
Detailed local climate projections have mostly been available to a few well-funded labs. Cheaper simulations could put flood, storm and heat risk data in front of city planners, insurers, farmers and teachers far sooner.

Source: [Hugging Face Blog (Ai2) ↗](https://huggingface.co/blog/allenai/hiro-acev2)

---
## Quick Hits

### Experts: AI "hacking" incidents come down to basic security lapses

Security experts quoted by CSO Online argue that recent reports of AI agents hacking systems aren't about AI going rogue — they're about AI labs skipping basic containment and monitoring. If your organisation runs AI agents, the lesson is familiar: limit what they can reach and watch what they do.

Source: [CSO Online ↗](https://www.csoonline.com/article/4234854/ai-agents-arent-going-rogue-frontier-labs-are-skipping-security-basics.html)

### Google is quietly linking your phone number across accounts

Android Authority reports that Google is automatically linking your phone number to every Google account signed in on your phone, without asking. If you keep separate work and personal accounts on one device, they may now be tied together by your number.

Source: [Android Authority ↗](https://www.androidauthority.com/google-auto-phone-number-verification-android-3723117/)

### OpenCode 2.0 is out

OpenCode, an open-source AI coding assistant, has released version 2.0, and it was one of the most discussed posts on Hacker News today. Open-source tools like this are an alternative to paid assistants from the big AI companies, letting teams choose which AI model sits behind them.

Source: [Hacker News ↗](https://anoma.ly/notes/opencode-2-0/)

### Security researcher: passkeys are not a trap

Security researcher Scott Helme pushes back on the worry that passkeys — sign-ins that use your phone or laptop's fingerprint, face or PIN instead of a password — lock you into one company's ecosystem. If you've been hesitating to switch on passkeys for work or personal accounts, it's a useful counterpoint.

Source: [Scott Helme ↗](https://scotthelme.co.uk/passkeys-are-not-a-trap/)

---
## Under the Hood

### GitHub rebuilds star history with 99% fewer requests

**What happened**
GitHub launched a new API for a repository's star history — how a project's popularity has grown over time. Instead of returning the list of individual people who starred a project, it returns trends, cutting the work needed from about 2,500 requests to 24.

**Why it matters**
It's a clean example of privacy and performance pulling in the same direction: by not exposing individual identities, GitHub also avoided unbounded database work. Useful reading for anyone designing analytics features over user activity.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/)

---
**Fun fact:** GitHub cut a feature's database work from 2,500 requests to just 24 — by asking for less.

*Daily tech digest for curious professionals. AI news that affects your work.*