# Daily Tech Digest — Thursday, July 30 2026

> The AI build-out's biggest hiring story isn't happening in offices — companies are recruiting electricians and carpenters by the thousands.

---
## AI Companies Are Recruiting Electricians and Carpenters by the Thousands

**What happened**
AI companies are recruiting and training skilled tradespeople — electricians, carpenters and others — in the thousands to build the data centres their models run on.

**What this means**
The clearest near-term job effect of the AI boom is showing up in construction and the trades, not in knowledge work. If you advise on careers, hiring or training — teachers, recruiters, managers — this is where demand is actually moving right now.

Source: [The New York Times ↗](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html)

---
## Quick Hits

### AI's Biggest Startups Have Nearly Stopped Publishing Their Research

Science reports that the leading AI startups now publish very little of the research behind their models. That makes it harder for outside experts to check company claims about what these systems can and can't do — so treat performance numbers you see in marketing with some caution.

Source: [Science ↗](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)

### Allen AI Opens Up Satellite Analysis at Planetary Scale

The Allen Institute for AI described OlmoEarth, the system it built to run AI analysis over satellite imagery of the entire planet. The point is to make questions like where forests are shrinking or which fields are flooded answerable at scale rather than one region at a time.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/olmoearth-infrastructure)

### Long Rulebooks Don't Reliably Keep AI Agents in Line

A new paper tested whether lengthy written policy documents actually govern how AI agents behave, and found they don't do it reliably. If your organisation is relying on a long instruction file to keep an AI assistant inside the rules, expect it to drift — and build real checks instead.

Source: [arXiv ↗](https://arxiv.org/abs/2607.25398)

### The US Science Agency Pilots Four-Year PhDs With Industry Placements

The National Science Foundation is piloting a programme with universities and companies to shorten doctorates to four years, with research placements in industry along the way. It's a direct response to how long research training takes compared with how fast the field moves.

Source: [National Science Foundation ↗](https://www.nsf.gov/news/nsf-partners-universities-industry-pilot-initiative-four)

---
## Under the Hood

### A 26-Billion-Parameter Model Running in 2 GB of RAM on a Mac

**What happened**
A developer released an open-source engine that runs Gemma 4 26B — a fairly large open model — inside 2 GB of memory on any M-series Mac. Normally a model that size needs many times that much RAM, so it stays on servers or high-end workstations.

**Why it matters**
Squeezing a large model onto ordinary consumer hardware means the work can happen on your own machine, with nothing sent to a company's servers. That's the practical route to private, offline AI for anyone handling sensitive material.

Source: [GitHub ↗](https://github.com/drumih/turbo-fieldfare)

### Taming the Flood of Automated Dependency Updates

**What happened**
GitHub published a practical guide to configuring Dependabot, the tool that automatically proposes updates to the third-party code a project depends on. Its defaults can bury a repository in update requests, so the guide covers grouping related updates together and slowing the general cadence while keeping security fixes immediate.

**Why it matters**
Update noise is a security problem, not just an annoyance: when there are too many routine requests to review, the urgent ones get missed. Separating 'keep current' from 'fix now' is what makes the alerts worth reading.

Source: [GitHub Blog ↗](https://github.blog/security/supply-chain-security/tame-dependabot-group-your-updates-slow-the-cadence-keep-security-fast/)

---
**Fun fact:** An open-source project now runs a 26-billion-parameter AI model in just 2 GB of memory.

*Daily tech digest for curious professionals. AI news that affects your work.*