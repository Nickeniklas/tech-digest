# Daily Tech Digest — Friday, September 18 2026

> Anthropic released two new flagship models today, OpenAI went straight after legal work, and Waymo's driverless taxis are heading to Singapore.

---
## Anthropic releases Claude Fable 5.1 and Claude Mythos 5.1

**What happened**
Anthropic released two new models, Claude Fable 5.1 and Claude Mythos 5.1, aimed at coding and knowledge work. The company says their research abilities are an early sign of how AI models will start contributing to scientific work.

**What this means**
"Knowledge work" is the part that matters for most people: drafting, analysis, research and summarising are exactly what these models are being tuned for. If you already use an AI assistant for writing or reviewing documents, expect the tools built on top of it to get noticeably steadier over the next few months.

Source: [Anthropic ↗](https://www.anthropic.com/claude-fable-and-mythos-5-1)

---
## Quick Hits

### OpenAI launches Astra, a product built for legal work

OpenAI announced Astra for Law, a version of its technology aimed specifically at legal professionals. It is the clearest sign yet that the big AI labs are going after individual professions rather than selling one general-purpose assistant to everyone. If you work in or near law, expect your firm's software vendors to start responding to this within the year.

Source: [OpenAI ↗](https://openai.com/index/astra-for-law/)

### Waymo's driverless taxis are going to Singapore

Waymo announced it is bringing its self-driving service to Singapore, its first move into Asia. Singapore's compact, tightly regulated road network makes it an unusually controlled place to test the technology. Robotaxis have spent years as a US coastal-city story; that is starting to change.

Source: [Waymo ↗](https://waymo.com/waymo-in-singapore/)

### A marketing team put its event process into code — and automated it

A GitHub marketer wrote up how their APAC team turned event planning and follow-up into automated workflows, on the argument that if you can write down how you do your work, you can automate it. It is a practical look at what "automate the boring parts" actually means for a non-engineering team. The same logic applies to onboarding, reporting, or any process you already document.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/)

### A 27-billion-parameter model squeezed into a ninth of the space

Researchers released Bonsai 2 27B, a compressed model they say keeps almost all of the original's quality in a footprint nine times smaller. Smaller footprints are what move AI off rented servers and onto ordinary hardware. That matters if your organisation has reasons — cost, privacy, or regulation — to keep data on its own machines.

Source: [PrismML ↗](https://prismml.com/news/bonsai-2-27b)

---
## Under the Hood

### GitHub rewrote the Copilot runtime in Rust — 800,000 lines of it

**What happened**
GitHub moved the runtime behind Copilot to Rust, ending up with roughly 800,000 lines of production code, and used Copilot itself to do much of the porting. The team's framing is blunt: a rewrite at this scale simply wasn't affordable before coding agents existed.

**Why it matters**
Large rewrites are usually rejected on cost, not merit — the engineering time is impossible to justify against shipping features. If agents genuinely change that maths, a category of work that teams have been deferring for a decade becomes possible again. The open question is how much review effort the 800,000 lines still demanded.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)

### Your AI agent passed the test. Will it pass it again?

**What happened**
IBM researchers argue that almost nobody reports the metric that matters most for agents: consistency. An agent can complete a task correctly once and fail the identical task on the next run, because some of its decisions sit on a knife edge rather than resting on a clear best option. The write-up walks through diagnosing which decisions are unstable and applying guidelines that reduce the gap without costing accuracy.

**Why it matters**
If you are putting an agent into a workflow that runs many times a day, a single successful demo tells you close to nothing. The useful number is the pass rate across repeated runs of the same task — and measuring it is cheap compared to discovering the variance in production.

```python
results = [run_agent(task) for _ in range(20)]
pass_rate = sum(r.success for r in results) / len(results)
print(f"passed {pass_rate:.0%} of 20 identical runs")
```

Source: [Hugging Face / IBM Research ↗](https://huggingface.co/blog/ibm-research/altk-evolve-consistency)

---
**Fun fact:** A Telstra network outage last week traced back to part of the network deciding the year was 2006.

*Daily tech digest for curious professionals. AI news that affects your work.*