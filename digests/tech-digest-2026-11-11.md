# Daily Tech Digest — Wednesday, November 11 2026

> Seven months into an AI-powered hunt for software security flaws, the people who have to fix them say the flood of reports is creating more work than it saves.

---
## AI bug-hunting project Glasswing is swamping volunteer maintainers, report says

**What happened**
Security firm VulnCheck reviewed seven months of Project Glasswing, Anthropic's effort to use AI to find security flaws in widely used open-source software, and says it has overwhelmed the volunteers who maintain that software with findings that are mostly underwhelming.

**What this means**
Finding problems with AI is cheap; checking and fixing them still takes human time. If your team uses AI to review contracts, code or reports, the same lesson applies: more flagged issues only help if someone can sort the real ones from the noise.

Source: [VulnCheck ↗](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

---
## Quick Hits

### From a health worker's notebook to the Ebola response

Anthropic published 'The Situation Report', a feature on the Ebola response in eastern Democratic Republic of the Congo. It follows how a community health worker's daily notes on fevers, recoveries and deaths — texted over WhatsApp — become the data responders rely on to make decisions.

Source: [Anthropic ↗](https://www.anthropic.com/features/ebola-response)

### People use AI to find news, but don't want it writing the news

Nieman Lab reports that AI is becoming a common gateway to information, yet audiences still don't want AI producing the journalism itself. If you work in media, communications or marketing, that gap between convenience and trust is worth keeping in mind.

Source: [Nieman Lab ↗](https://www.niemanlab.org/2026/11/ai-is-becoming-an-information-gateway-audiences-still-dont-want-it-making-their-news/)

### Hugging Face can now go on your Google Cloud bill

Organizations can link their Hugging Face account to Google Cloud so usage appears on their existing Google Cloud bill instead of a credit card. For teams, that can mean skipping a separate procurement process to start using AI models hosted there.

Source: [Hugging Face ↗](https://huggingface.co/blog/hub-gcp-marketplace)

### A large study measures how easily websites can recognise you

A new study looks at how 'fingerprintable' web users are — how easily sites can identify you from details of your browser and device, without cookies. It's a reminder that clearing cookies alone doesn't make you anonymous online.

Source: [fingerprinting.study ↗](https://fingerprinting.study/)

---
## Under the Hood

### Git patches six security vulnerabilities

**What happened**
Git, the version-control tool almost all software teams use to track changes, released updates fixing six security vulnerabilities. They affect recursive clones, reference handling, merges, binary patches and imports.

**Why it matters**
Cloning and merging are everyday operations, so developers and automated build systems that handle code from outside sources should update Git promptly.

```python
git --version
# Compare with the patched versions listed in the advisory,
# then update via your package manager, e.g.:
# brew upgrade git   or   sudo apt upgrade git
```

Source: [GitHub Blog ↗](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/)

### Hugging Face adds 'decision models' for problems that aren't about text

**What happened**
Hugging Face introduced Decision Models, starting from the point that large language models excel at generating text but many problems don't need text at all — they need a choice, a score or an action.

**Why it matters**
Using a smaller model built to make decisions can be cheaper and more predictable than prompting a chatbot, which matters for teams building classification, routing or recommendation features.

Source: [Hugging Face ↗](https://huggingface.co/blog/decision)

---
**Fun fact:** GitHub's Game Off jam is running for the 14th year — this November's theme is SHIFT.

*Daily tech digest for curious professionals. AI news that affects your work.*