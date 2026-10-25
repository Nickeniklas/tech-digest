# Daily Tech Digest — Sunday, October 25 2026

> America has lost about 200,000 jobs in media, film and the arts — and one economist is trying to work out how much of that is down to AI.

---
## How much of the creative job slump is AI?

**What happened**
Economics newsletter Apricitas looks at the roughly 200,000 jobs the US has lost in media, film and the arts, and asks how much of that decline AI can actually explain.

**What this means**
If you work in writing, design, marketing or production, this is the question behind a lot of nervous conversations. A look at the actual job numbers helps separate what AI is changing from what other industry shifts are driving.

Source: [Apricitas Economics ↗](https://www.apricitas.io/p/ai-and-the-fall-of-the-creative-class)

---
## Quick Hits

### Terence Tao launches a hub to check OpenAI's math write-ups

Mathematician Terence Tao announced oai-math-revised, a community project where people can review and revise the write-ups OpenAI has published about math results. It's a practical example of experts double-checking AI-produced work in public rather than taking it on trust.

Source: [Terence Tao's blog ↗](https://terrytao.wordpress.com/2026/10/24/oai-math-revised-a-community-hub-for-revising-openais-math-write-ups/)

### A security flaw spreads to many web software libraries

Security firm Aikido reports that a vulnerability known as Node2Shell has evolved into HTTP2Shell, and now affects many libraries and apps that handle web traffic, including Python packages. If your team runs its own web services, it's worth asking your developers whether they've checked for it.

Source: [Aikido ↗](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)

### How three Java experts use GitHub Copilot day to day

GitHub asked three Java Champions — recognised experts in the Java programming language — how they use its Copilot AI assistant. Their common thread: use it to solve problems and move faster, but keep humans responsible for the results.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-3-java-champions-are-using-github-copilot-for-increased-productivity/)

### Roku moves its developer projects from GitHub to GitLab

Roku says its developer code repositories have moved from GitHub to GitLab, a competing platform. It's a reminder that even big companies are reconsidering where their code lives.

Source: [Roku Developer Blog ↗](https://blog.roku.com/developer/gitlab-move)

---
## Under the Hood

### ThinkingBox: training AI agents by checking the database, not their word

**What happened**
Microsoft released ThinkingBox-Training on GitHub, a follow-up to its earlier post 'The Agent Said It Was Done. The Database Disagreed.' Instead of trusting an agent's claim that it finished a task, the system grades what actually changed in the database and turns that grade into a reward for reinforcement learning — a training method where the model learns from scores.

**Why it matters**
Agents that say they're done when they aren't are one of the biggest practical problems with AI automation. Grading the real outcome gives developers a more honest training signal for agents that work with business data.

```python
# Illustration: reward based on real database state, not the agent's claim
def reward(db, expected_rows):
    actual = db.execute("SELECT * FROM orders").fetchall()
    return 1.0 if sorted(actual) == sorted(expected_rows) else 0.0
```

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/microsoft/thinkingbox-training)

### Cerebras explains how it runs trillion-parameter models

**What happened**
AI chipmaker Cerebras published a write-up on how it deploys frontier AI models with around a trillion parameters — the internal settings a model learns during training — on its own hardware.

**Why it matters**
Models this large are usually spread across many GPUs. Cerebras builds very large chips instead, and its account shows one alternative route to serving the biggest models.

Source: [Cerebras ↗](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)

---
**Fun fact:** St. Helena's 5 pence coin features Jonathan, a tortoise roughly 190 years old.

*Daily tech digest for curious professionals. AI news that affects your work.*