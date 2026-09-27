# Daily Tech Digest — Sunday, September 27 2026

> A teacher watched AI finish every homework assignment they set — and rebuilt how they teach instead of banning it.

---
## A teacher rethinks the job after AI did all the homework

**What happened**
A teacher wrote up what they changed after finding that AI could complete every one of their homework assignments. The essay is one of the most-discussed pieces on Hacker News today.

**What this means**
If take-home work can be done by a chatbot, it no longer shows you what someone actually knows. Teachers are the obvious audience, but the same question applies to anyone who assesses work: hiring managers setting take-home tests, trainers running certifications, editors reviewing drafts.

Source: [The Last Software Engineer ↗](https://thelastsoftwareengineer.substack.com/p/how-i-changed-teaching-after-ai-managed)

---
## Quick Hits

### ASML says it sold "absolutely nothing" in Europe this year

ASML, the Dutch company that makes the machines used to produce the world's most advanced chips, says it has sold nothing in Europe in 2026 and is asking the EU to help create demand. It's a blunt sign that Europe's plan to build more of its own chips hasn't turned into factory orders yet.

Source: [Tom's Hardware ↗](https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand)

### One Twitch chat message was enough to take over a streamer's PC

Security researchers describe how a single message typed into a Twitch chat ended up running code on the streamer's own computer. If you stream, or use tools that react to chat, it's a reminder that anything that reads public messages can be a way in.

Source: [SCRT ↗](https://blog.scrt.ch/2026/09/22/how-one-twitch-chat-message-became-code-execution-on-a-streamers-pc/)

### GitHub shows beginners how to build their own AI workspaces

Previously covered on 2026-09-25: GitHub argued that a chat box is sometimes the wrong way to work with AI. Since then, it has published a beginner's guide: you describe the interface you want in plain English, and the Copilot agent builds a live "canvas" you can both use and update.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/)

### New signs that Saturn's moon Enceladus could support life

Researchers at Freie Universität Berlin report promising findings, drawn from Cassini spacecraft data, about the potential for microbial life on Enceladus, one of Saturn's icy moons. It adds weight to the case for sending a dedicated mission there.

Source: [Freie Universität Berlin ↗](https://www.fu-berlin.de/en/presse/informationen/fup/2026/fup_26_116-enceladus-cassini-mikroben-science-postberg/index.html)

---
## Under the Hood

### Your AI agent passed once. Will it pass again?

**What happened**
IBM Research published a piece on consistency in AI agents: an agent that completes a task on one run may fail the same task on the next. Most benchmarks report a single success, which hides that variation.

**Why it matters**
If you're deploying an agent for real work, reliability across repeated runs matters more than one good demo. Measuring a pass rate over many attempts gives a more honest picture than a single pass/fail.

```python
import random

def run_agent(task):
    return random.random() > 0.3  # stand-in for a real agent call

runs = [run_agent("book a meeting") for _ in range(20)]
print(f"Passed {sum(runs)}/{len(runs)} runs")
print("Consistent" if all(runs) else "Not consistent")
```

Source: [Hugging Face Blog (IBM Research) ↗](https://huggingface.co/blog/ibm-research/altk-evolve-consistency)

### Why shorter AI answers can cost more

**What happened**
GitHub explained how it makes Copilot's coding work cheaper without lowering quality, and why a shorter model output doesn't always mean a cheaper task. The focus is on cutting wasted work across the whole coding task, not just trimming individual replies.

**Why it matters**
For teams paying per use, the real cost is the total work an AI does to finish a job — including retries and dead ends — not the length of any one response.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)

---
**Fun fact:** Someone built fonts where every chunk of text an AI reads, called a token, takes up exactly the same width.

*Daily tech digest for curious professionals. AI news that affects your work.*