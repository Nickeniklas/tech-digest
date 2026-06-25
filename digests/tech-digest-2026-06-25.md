# Daily Tech Digest — Thursday, June 25 2026

> OpenAI now has its own chip — a sign that the companies building AI no longer want to depend on anyone else to run it.

---
## OpenAI Unveils Its First Custom Chip, Built With Broadcom

**What happened**
OpenAI revealed its first in-house AI chip, designed in partnership with Broadcom. The company that makes ChatGPT will now run more of its systems on hardware it controls, rather than relying entirely on chips bought from Nvidia.

**What this means**
The tools you use are built on a small number of suppliers, and the biggest AI firms are racing to own that foundation. If OpenAI can make its own chips, it gains more control over cost, supply, and speed — which over time affects the price and reliability of the AI products you pay for.

Source: [TechCrunch ↗](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

---
## Quick Hits

### Google's Gemini Can Now Operate a Computer for You

Google added a feature to its Gemini 3.5 Flash model that lets it use a computer the way a person does — clicking buttons, filling in forms, and moving through web pages on your behalf. It is meant for routine, multi-step tasks like booking or data entry. This is the same direction every major AI company is now heading: assistants that act, not just answer.

Source: [Google ↗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

### Cloudflare Makes a Common Login System Free for Everyone

Cloudflare released self-managed OAuth — the technology behind 'Sign in with Google' style buttons — for all of its users at no cost. It lets any website or app add secure, standard logins without building the plumbing from scratch. For small teams and solo builders, it removes a tedious and error-prone piece of work that often goes wrong.

Source: [Cloudflare ↗](https://blog.cloudflare.com/oauth-for-all/)

### Krea 2 Is a New Open Image Model Anyone Can Run

Krea released Krea 2, a 12-billion-parameter image generator whose weights are open, meaning anyone can download and run it rather than paying for access through a single company's service. The team says it competes with the best closed image tools. For designers and marketers, open models mean more options that can run privately, without sending your work to someone else's servers.

Source: [Krea ↗](https://www.krea.ai/blog/krea-2-technical-report)

### A Cooling Design That Nearly Eliminates Data-Center Water Use

Nvidia detailed a liquid-cooling approach for AI data centers that runs at a warmer 45°C, which lets the facility shed heat without the constant water evaporation that traditional cooling relies on. The result is near-zero water consumption. Data centers' thirst for water has become a real concern in dry regions, so this matters well beyond the tech industry.

Source: [Nvidia ↗](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/)

---
## Under the Hood

### Git Worktrees: One Repository, Several Branches at Once

**What happened**
GitHub published a practical guide to git worktrees, a feature that has existed since 2015 but has become popular again. A worktree lets you check out multiple branches of the same project into separate folders simultaneously, so you can work on a new feature in one folder while keeping a bug fix open in another — no stashing, no switching back and forth.

**Why it matters**
The recent surge of interest is tied to AI coding agents: you can point a different agent at each worktree and let several run in parallel without them stepping on each other. For developers juggling multiple tasks, it removes a constant source of friction.

```python
git worktree add ../feature-login feature/login
cd ../feature-login
# now this folder is on the feature/login branch,
# while your main folder stays on main
git worktree list
git worktree remove ../feature-login
```

Source: [The GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

### GitHub Adds Limits to Cut Down Pull-Request Spam

**What happened**
GitHub introduced pull-request limits that let maintainers cap how many open contributions a single person can have at once. The change responds to a wave of low-quality, often AI-generated submissions that have been flooding popular open-source projects and burying genuine work.

**Why it matters**
Open-source maintainers are mostly volunteers, and reviewing junk submissions burns the time they have. Throttling the volume is a blunt but practical defense — and a sign of how teams are adapting their processes as automated contributions become common.

Source: [The GitHub Blog ↗](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

---
**Fun fact:** A new data-center cooling design runs warm, at 45°C, and that single change cuts its water use to nearly zero.

*Daily tech digest for curious professionals. AI news that affects your work.*