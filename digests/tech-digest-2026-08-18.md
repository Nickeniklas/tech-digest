# Daily Tech Digest — Tuesday, August 18 2026

> Anthropic's newest top-tier model arrives at half the price of its biggest one — the latest sign that serious AI work is getting cheaper, not more expensive.

---
## Anthropic Releases Claude Opus 5

**What happened**
Anthropic released Claude Opus 5, the newest model in its high-end tier. The company says it comes close to the intelligence of its largest model, Claude Fable 5, at half the price, with improvements in coding and in long-running tasks an assistant works through over hours rather than seconds.

**What this means**
The expensive end of AI keeps getting cheaper, which changes what is worth handing over: work that was too costly to automate a few months ago may be routine now. If you have tested AI on drafting, research, or document review and shelved it on cost, it is worth pricing again.

Source: [Anthropic ↗](https://www.anthropic.com/news/claude-opus-5)

---
## Quick Hits

### OpenAI Halves the Price of GPT-5.6 Sol

OpenAI cut the price of its GPT-5.6 Sol model by 50%. Separately, testers report it is the strongest model the company has released at reading images — charts, scanned documents, photographs. Cheaper image handling matters if your work involves paperwork that arrives as pictures rather than text.

Source: [OpenRouter ↗](https://openrouter.ai/openai/gpt-5.6-sol)

### An AI Bug-Fixing Tool Was Turned Into a Way In

Security firm Wiz describes how GitHub Copilot's "Autofix" feature — which proposes code fixes automatically — could be manipulated to compromise Snowflake's internal Jira system. The attack worked by feeding the tool instructions hidden in content it was asked to read. It is a concrete example of a growing problem: an assistant that acts on text it finds can be steered by whoever wrote that text.

Source: [Wiz ↗](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

### A Fake Think Tank Built to Influence Chatbots

Responsible Statecraft reports that Israel set up a think tank that appears to exist mainly so AI chatbots will cite it. Because assistants answer by drawing on what is published online, planting authoritative-looking sources is a way to shape their answers. If you rely on a chatbot for background research, the citation is worth clicking.

Source: [Responsible Statecraft ↗](https://responsiblestatecraft.org/israel-influence-chatgpt/)

### A Librarian's Guide to Turning AI Off

Librarian Jessamyn West published a practical list of how to disable or avoid the AI features now switched on by default in search engines, browsers, phones, and office software. It is written for people who never asked for them. Useful if you want the choice back, or need to explain the settings to colleagues or clients.

Source: [librarian.net ↗](https://www.librarian.net/notoai/)

---
## Under the Hood

### Same Machines, 33 Points More Use — Only the Order Changed

**What happened**
A team writing on Hugging Face's blog describes running the same cluster of AI chips 33 percentage points closer to full use without buying anything, purely by changing the order jobs run in. The default approach is first-come, first-served, which stalls when demand exceeds supply; replacing it with an allocator that knows each job's priority and deadline fills the idle gaps. The authors are blunt that it only works if the demand estimates feeding it are honest.

**Why it matters**
GPUs are the main cost of running AI, and idle ones are pure loss. This is a reminder that a lot of AI infrastructure spending is a scheduling problem before it is a hardware problem — relevant to anyone signing off on compute budgets.

Source: [Hugging Face ↗](https://huggingface.co/blog/Dharma-AI/gpu-management-pt2)

### DuckDB Previews Version 2.0

**What happened**
DuckDB published a preview of the highlights coming in version 2.0. DuckDB is a small, free database that runs inside whatever program you are already using — no server to install or administer — and it has become a common way to query large spreadsheets and data files directly on a laptop.

**Why it matters**
It sits in the gap between a spreadsheet that chokes on a million rows and a full database that needs a team to run it. For analysts and researchers, a major version is worth watching: the same file that was too big to open becomes a query you run in a second.

```python
import duckdb

duckdb.sql("SELECT region, SUM(amount) FROM 'sales.csv' GROUP BY region").show()
```

Source: [DuckDB ↗](https://duckdb.org/2026/08/17/duckdb-20-highlights)

---
**Fun fact:** Researchers confirmed the first known death by trebuchet, from a shattered skeleton found at a Scottish castle.

*Daily tech digest for curious professionals. AI news that affects your work.*