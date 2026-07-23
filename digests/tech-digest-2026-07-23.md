# Daily Tech Digest — Thursday, July 23 2026

> One of the world's most respected mathematicians sat down to check whether an AI really cracked a decades-old math problem — and showed his work in public.

---
## A Top Mathematician Checks the AI's Claimed Math Breakthrough

**What happened**
Previously covered on 2026-07-20: a counterexample to the long-unsolved Jacobian Conjecture was reportedly produced with help from Claude Fable, one of Anthropic's newest models. Since then, Terence Tao — widely regarded as one of the greatest living mathematicians — worked through the claim in a public conversation, examining step by step whether the AI's proposed answer actually holds up.

**What this means**
This is a preview of how expert work is starting to change: an AI can now propose a serious result, but a human specialist still does the careful checking. For anyone whose job involves judgment — lawyers, doctors, analysts, teachers — the pattern is the same, AI drafts, and a qualified person verifies before anyone trusts it.

Source: [Terence Tao (public conversation) ↗](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56)

---
## Quick Hits

### GitHub Now Charges Copilot Users the Same Rates as the Raw AI

GitHub is changing how it bills its Copilot coding assistant, passing along the underlying AI model costs at the same listed rates you'd pay to use those models directly. The company argues that what you're really paying for is the workflow, policies, and safeguards built around the model, not just access to it. If you pay for AI tools at work, expect more providers to make this 'you're paying for the wrapper' argument as raw model prices become public.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/copilot-vs-raw-api-access-what-are-you-actually-paying-for/)

### GitHub Overhauls the Program That Pays Hackers to Find Bugs

GitHub is restructuring its 'bug bounty' program — the system that pays independent security researchers to report flaws instead of exploiting them. The changes are meant to give researchers a smoother experience working with GitHub's team. Bug bounties are a quiet but important part of why the software you rely on stays reasonably safe.

Source: [GitHub Blog ↗](https://github.blog/security/next-chapter-restructuring-githubs-bug-bounty-program/)

### Tech Commentator John C. Dvorak Has Died

John C. Dvorak, one of the most recognizable technology columnists and podcasters of the personal-computer era, has died. For decades he was a fixture of tech magazines and later podcasts, known for blunt, contrarian takes on the industry. His death marks the passing of a voice that shaped how a generation of ordinary readers talked about computers.

Source: [Announcement ↗](https://twitter.com/na_announce/status/2079952538040672302)

### A New Tool Teaches a Small AI Model to Know When It's Wrong

Developers released Cactus Hybrid, a system that trains a compact AI model to recognize when it isn't confident and hand the question off to a more capable model instead of guessing. The goal is to cut down on the confident-but-wrong answers that erode trust in AI. It's a small step toward assistants that admit uncertainty rather than bluff.

Source: [Cactus Compute (GitHub) ↗](https://github.com/cactus-compute/cactus-hybrid)

---
## Under the Hood

### GigaToken: Making the First Step of AI Text Processing Far Faster

**What happened**
Before an AI model reads your text, that text is broken into small pieces called tokens — a step called tokenization. A new open-source project, GigaToken, reworks how this is done and reports tokenizing text roughly 1,000 times faster than the standard approach. It targets the pipelines that prepare enormous amounts of text for training and running large models.

**Why it matters**
Tokenization is unglamorous plumbing, but at the scale of billions of documents it can become a real bottleneck and cost. Speeding it up means teams spend less time and money just preparing data before any actual AI work begins. This is aimed at engineers building or feeding large models.

Source: [GigaToken (GitHub) ↗](https://github.com/marcelroed/gigatoken/)

### Running Hugging Face Models at Full Speed Inside vLLM

**What happened**
Hugging Face and the vLLM project detailed a new backend that lets models defined in the popular Transformers library run at native speed inside vLLM, a system built to serve AI models to many users quickly. Previously, using a Transformers-style model this way often meant a performance penalty; this closes much of that gap.

**Why it matters**
For teams that deploy open models themselves rather than renting them from a cloud provider, this reduces the tradeoff between convenient, well-supported model code and fast, efficient serving. In plain terms: fewer servers to answer the same number of requests. This is for the people running AI in production.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/native-speed-vllm-transformers-backend)

---
**Fun fact:** Beekeepers can now track a hive's health by having AI listen to the sound of its buzzing.

*Daily tech digest for curious professionals. AI news that affects your work.*