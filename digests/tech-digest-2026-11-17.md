# Daily Tech Digest — Tuesday, November 17 2026

> Running open AI models just got simpler: Hugging Face, the main library of free models, is teaming up with a service that sends your request to whichever of 80+ providers is working best right now.

---
## Hugging Face and OpenRouter team up to make open AI models easy to use

**What happened**
Hugging Face, where nearly every major open-weight AI model is published, is partnering with OpenRouter, a service that runs those models at scale and routes each request across more than 80 providers based on live measurements of how each one is performing.

**What this means**
Open models — ones anyone can download and use — have often been harder to try than ChatGPT or Claude. If your team wants a cheaper or more private alternative, this lowers the effort of testing one without setting up servers yourself.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/openrouter)

---
## Quick Hits

### Report: Windows 11 tracks which AI coding tools you use

A developer's blog post, widely discussed on Hacker News, says Windows 11 collects data on which coding agents and developer tools are installed and used on a machine. If your organization has policies on what usage data leaves company laptops, this is worth passing to your IT team.

Source: [xusheng.dev ↗](https://xusheng.dev/posts/windows-coding-agent-telemetry/)

### Optimizely breach served malware on major sites, including Zoom and GitLab

Report URI says Optimizely — a widely used tool companies add to their websites to test different page designs — was compromised and used to deliver malware through brands such as Zoom and GitLab. It's a reminder that a website is only as safe as every outside tool it loads, which matters for anyone in marketing who adds tracking or testing scripts.

Source: [Report URI ↗](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

### Carnegie Mellon puts computer science courses on YouTube for free

Carnegie Mellon University, one of the top computer science schools in the US, is publishing its computer science courses on YouTube at no cost. Teachers and anyone curious about how the technology behind AI works now have a free, high-quality place to start.

Source: [Carnegie Mellon University ↗](https://www.cs.cmu.edu/learn/)

### Anthropic maps out possible futures for an AI economy

Anthropic published 'Scenarios for our economic future', starting from an honest premise: nobody yet knows whether AI will bring unprecedented growth, widespread unemployment, neither, or something else. The piece asks how we would be able to tell which path we are on — useful framing if you're planning your own career or team around AI.

Source: [Anthropic ↗](https://www.anthropic.com/institute/econ-scenarios)

---
## Under the Hood

### GitHub rebuilds Git storage so thousands of AI agents can work in one project

**What happened**
GitHub described a new architecture for storing Git repositories, built so that thousands of AI agents can push changes to a single repository at the same time. Git is the system software teams use to track every change to their code; it was designed around a handful of humans committing occasionally, not swarms of automated workers.

**Why it matters**
It shows how platforms are being re-engineered on the assumption that most future code changes will come from agents rather than people. For engineering leaders, it signals that agent-heavy workflows are moving from experiment to infrastructure that GitHub expects to support at scale.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)

---
*Daily tech digest for curious professionals. AI news that affects your work.*