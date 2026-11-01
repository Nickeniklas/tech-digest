# Daily Tech Digest — Sunday, November 1 2026

> Lawyers in Brazil were sanctioned for hiding instructions to AI inside a court filing — a sign that courts are starting to treat tricking AI as misconduct.

---
## Anthropic maps out possible futures for an AI-shaped economy

**What happened**
Anthropic published 'Scenarios for our economic future', starting from a frank admission: nobody yet knows whether AI will bring unprecedented growth, widespread unemployment, neither, or something else. The piece lays out different possible paths and asks how we could tell which one we're on.

**What this means**
If you're planning a career, a team, or a budget around AI, this is a reminder that even the companies building it don't claim to know the outcome. Managers and HR leaders in particular can use scenario thinking like this to prepare for more than one future instead of betting on a single forecast.

Source: [Anthropic ↗](https://www.anthropic.com/institute/econ-scenarios)

---
## Quick Hits

### Brazilian court sanctions lawyers for prompt injection in a filing

A Brazilian court has sanctioned lawyers for prompt injection — hiding instructions in a document meant to manipulate any AI that reads it — in a court filing. It's an early sign that courts see attempts to steer AI-assisted review as professional misconduct. If you're a lawyer, treat hidden text in filings the same way you'd treat any attempt to mislead the court.

Source: [Jetstream Security ↗](https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/)

### ChatGPT and Codex usage limits are merging

OpenAI published a help article explaining that usage limits for ChatGPT and Codex, its coding assistant, are being merged. If you use both, check how the shared allowance works so heavy use of one doesn't unexpectedly cut into the other.

Source: [OpenAI Help Center ↗](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)

### Researchers describe taking over ChatGPT accounts

Security firm Parameter published a write-up titled 'Do the math: How we took over ChatGPT accounts', describing a gap they found at OpenAI. It's a good moment to make sure your AI accounts use strong, unique passwords and two-factor authentication, especially if they hold work conversations.

Source: [Parameter ↗](https://www.parameter.ai/labs/we-found-a-gap-at-openai)

### How AI helps turn field notes into Ebola situation reports

Anthropic's feature 'The Situation Report' follows community health workers in eastern Democratic Republic of the Congo, whose handwritten counts of fevers, recoveries and deaths travel by WhatsApp and become the data responders rely on. It shows how AI is being used in the unglamorous but vital work of organising messy real-world information.

Source: [Anthropic ↗](https://www.anthropic.com/features/ebola-response)

---
## Under the Hood

### Critical Linux networking flaw scores 9.8 out of 10

**What happened**
A write-up details CVE-2026-98432, a use-after-free bug — where software keeps using memory it has already released — in the Linux kernel's IPv4 TCP code, the part that handles most internet connections. It carries a CVSS severity score of 9.8 out of 10.

**Why it matters**
TCP code runs on almost every Linux server, phone and device, so a critical flaw there is broad in reach. If you manage servers, watch for kernel updates from your distribution and apply them promptly.

Source: [Atlasum ↗](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)

### A team of five small open models beats Fable 5 on hard coding tests

**What happened**
The open-source Memdoor project shows a workflow where five copies of Qwen3.8-27B, a mid-sized open model, work together as a team and outperform Fable 5 on the hard tier of LiveCodeBench, a coding benchmark.

**Why it matters**
It's more evidence that coordinating several smaller, downloadable models can rival a single top-tier model on specific tasks — useful for teams that want to run AI on their own hardware or control costs.

Source: [Memdoor on GitHub ↗](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve)

---
**Fun fact:** The Arecibo telescope's 2020 collapse traced back to zinc slowly creeping out of its cable sockets.

*Daily tech digest for curious professionals. AI news that affects your work.*