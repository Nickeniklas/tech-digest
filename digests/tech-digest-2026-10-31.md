# Daily Tech Digest — Saturday, October 31 2026

> A tampered copy of a popular AI coding assistant turned up in an extension store, a reminder that the tools you install deserve the same caution as the emails you open.

---
## Backdoored Claude Code extension found on the Cursor Marketplace

**What happened**
Security firm Phorion reports that a version of the Claude Code extension for VS Code, listed on the Cursor Marketplace, had been compromised with a backdoor: hidden code that can give an attacker access to the computer it is installed on.

**What this means**
AI assistants that plug into your editor, browser or office apps can usually see your files and run actions on your behalf, so a fake or tampered copy is a serious risk. Install extensions only from the official publisher, and if your team uses AI coding tools, ask IT to check which versions are installed.

Source: [Phorion ↗](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

---
## Quick Hits

### Cisco gives one engineer unlimited AI to rewrite old code

Fortune reports that Cisco president Jeetu Patel has given a 27-year-old engineer unlimited AI usage to rewrite the company's legacy code. The story feeds a wider debate about what AI means for entry-level jobs: fewer junior roles, or junior staff doing far bigger work than before.

Source: [Fortune ↗](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/)

### AI isn't replacing site reliability engineers — it's deskilling them

An essay from the SigNoz newsletter argues that AI isn't taking jobs from the engineers who keep websites and apps running, but is slowly eroding their skills as they hand off more of the hands-on work. The same worry applies to any profession: if AI does the routine parts, how do you stay sharp for the hard cases?

Source: [SigNoz ↗](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

### Police camera searches fell 95% after misconduct was caught

WKYC reports that searches of Flock licence-plate camera data in Highland Heights, Ohio dropped 95% after a police dispatcher's misconduct with the system was discovered. It's a striking sign of how much of a surveillance tool's use can depend on a single person's access.

Source: [WKYC ↗](https://www.wkyc.com/article/news/investigations/flock-camera-searches-fall-95-percent-highland-heights-dispatcher-misconduct-caught/95-94b18f33-60e2-4bc7-a00f-d71d1e1fdd5e)

### A grumpy AI pirate ship greets trick-or-treaters

For Halloween, a developer built MonsterHouse, an interactive projection that listens to trick-or-treaters and answers in the voice of a grumpy old pirate ship, softening when visitors remember their manners. It runs on NVIDIA's Nemotron voice and language models, showing how far small, off-the-shelf AI parts have come for hobby projects.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/nvidia/nemotron-halloween)

---
## Under the Hood

### GitHub moves its repositories to Azure for the agent era

**What happened**
GitHub says it has moved a copy of 99.99999% of its repositories to Microsoft's Azure cloud. A new post explains how per-reference quorums (a voting system that agrees on the latest state of each branch before accepting a change) will bring over the rest, and how object storage lets reading code scale separately from writing it.

**Why it matters**
AI coding agents read and write code far more often than people do, so the platform underneath has to handle much heavier traffic. This is the infrastructure work behind GitHub's push to become the home for agent-driven software development.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/)

### Google's 'Sleep' framework helps AI models keep what they learn

**What happened**
Google Research introduced the Sleep framework, a new approach to continual learning — teaching a language model new information over time without it forgetting what it already knew.

**Why it matters**
Today's models are mostly frozen after training, and updating them risks overwriting older knowledge. Methods like this are a step toward assistants that stay current without full, expensive retraining.

Source: [Google Research ↗](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)

---
**Fun fact:** A developer squeezed a working Nintendo into about 1GB of AI model weights.

*Daily tech digest for curious professionals. AI news that affects your work.*