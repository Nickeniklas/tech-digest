# Daily Tech Digest — Friday, November 20 2026

> An AI model just helped settle two open questions about black holes — and that says something about where AI research help is heading.

---
## Claude solves two open problems in black hole physics

**What happened**
Anthropic reports that Claude, its AI model, solved two open problems in the physics of black holes — questions researchers had not yet answered. The write-up is on Anthropic's research blog and drew wide discussion on Hacker News.

**What this means**
AI is moving from summarising existing knowledge to contributing new results in specialist fields. If you work in research, academia, or any field built on hard analysis, expect AI to become a working partner on open questions — with experts still needed to check the results.

Source: [Anthropic ↗](https://www.anthropic.com/research/claude-black-hole-physics)

---
## Quick Hits

### Critical security flaw found in OpenSSL

OpenSSL, the software that encrypts traffic for a huge share of websites and apps, has a buffer overflow bug rated 9.8 out of 10 for severity. A fix is in progress. You don't need to do anything yourself, but expect your IT team and software vendors to push updates soon — install them.

Source: [GitHub (OpenSSL) ↗](https://github.com/openssl/openssl/pull/33652)

### Visa, Mastercard and JPMorgan customer data leaked

The Wall Street Journal reports that hackers leaked customer data from Visa, Mastercard and JPMorgan. If you hold cards or accounts with these companies, watch your statements and be extra wary of emails or calls that claim to come from your bank.

Source: [The Wall Street Journal ↗](https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87)

### UK admits it secretly ordered Apple to weaken encryption

The UK government has been forced to admit it issued Apple a secret order about encryption — the technology that keeps your messages and files private. It matters for anyone handling confidential client or patient data, and for lawyers following how far governments can reach into private tech.

Source: [Mac Anorak ↗](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/)

### GitHub launches open-source projects for accessibility

GitHub introduced Replica and the Open Source Accessibility Framework, two new open-source projects aimed at collaboration and inclusion. If you design or manage digital products, these give teams a shared starting point for making software usable by more people.

Source: [GitHub Blog ↗](https://github.blog/open-source/maintainers/the-best-things-in-open-source-are-built-together/)

---
## Under the Hood

### Why AI fine-tuning jobs run longer than expected

**What happened**
A Hugging Face blog post analyses 272 real production runs to predict how long fine-tuning — retraining an AI model on your own data — actually takes on shared GPU clusters. The headline finding: the raw compute math (FLOPs) underestimates the real end-to-end time.

**Why it matters**
Teams budgeting for custom AI models often plan from compute estimates alone. A model built on real runs gives more honest timelines and cost forecasts for anyone scheduling training work.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time)

### PostgreSQL 19 is out

**What happened**
PostgreSQL 19, a new major version of one of the most widely used open-source databases, has been released. One highlighted feature is a built-in 'repack' that cleans up table bloat — wasted space that builds up as data changes — faster and without extra tools. Neon and Databricks Lakebase already offer it.

**Why it matters**
Many apps and AI products store their data in Postgres. Built-in bloat cleanup means less maintenance work and steadier performance for teams running large databases.

```python
-- Check your server version after upgrading
SELECT version();
```

Source: [PostgreSQL ↗](https://www.postgresql.org/docs/release/19.0/)

---
**Fun fact:** TCP/IP, the rules that let every computer on the internet talk to each other, was never patented.

*Daily tech digest for curious professionals. AI news that affects your work.*