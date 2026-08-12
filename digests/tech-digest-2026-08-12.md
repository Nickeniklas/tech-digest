# Daily Tech Digest — Wednesday, August 12 2026

> Live facial recognition is arriving on the London Underground, which moves the technology from borders and stadiums into an ordinary commute.

---
## London Underground Starts Scanning Passengers' Faces

**What happened**
British Transport Police are expanding their live facial recognition trial into London Underground stations, where cameras check passing faces against a watchlist in real time. Anyone the system flags can be stopped; everyone else is simply scanned on the way through.

**What this means**
Facial recognition is shifting from borders and big events into everyday travel, so questions about who ends up on a watchlist and how a wrong match gets corrected stop being hypothetical. If your work touches privacy policy, HR, or public-sector procurement, expect this to reach your desk before long.

Source: [British Transport Police ↗](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/)

---
## Quick Hits

### A Firm Selling "100% Human-Written" Research Was Using AI for All of It

404 Media reports that a company marketing medical research and peer review as never AI-generated was in fact producing it entirely with AI. The claim was the whole product, which makes this a plain case of misrepresentation rather than an argument about whether AI writing is acceptable. If you buy written work from an agency, the lesson is that "no AI" is a promise worth verifying.

Source: [404 Media ↗](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/)

### An Officer Is Accused of Using a Camera Network to Follow an Ex-Partner

A New Bedford police officer allegedly used Flock's automated licence plate camera network to track a former romantic partner. The cameras were installed to investigate crimes, so the case is really about what stops someone with legitimate access from using the system for something else. It is the same question every organisation faces once it holds data about where people go.

Source: [New Bedford Light ↗](https://newbedfordlight.org/new-bedford-police-officer-accused-of-using-flock-cameras-to-track-and-follow-ex-romantic-partner/)

### Researchers Test Whether AI Models Can Notice Their Own Thinking

A new paper looks at whether large language models can accurately report what is happening inside them, or whether they just produce a plausible-sounding story about it. The distinction matters if you rely on an AI tool's explanation of why it gave you a particular answer. A confident-sounding rationale is not evidence that the rationale is the real reason.

Source: [arXiv ↗](https://arxiv.org/abs/2601.01828)

### Mojo, the Python-Like Language Built for AI, Reaches 1.0

Modular shipped version 1.0 of Mojo, a language designed to read like Python while running much closer to hardware speed. A 1.0 release is the point where a language is considered stable enough to build production software on. For everyone else, it is a sign that the tools underneath AI products are maturing rather than being rewritten every few months.

Source: [Modular ↗](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)

---
## Under the Hood

### Two Ways to Let an Agent Learn From Itself — and What Each Costs in Tokens

**What happened**
IBM Research compared its ALTK-Evolve approach with ACE. Both let an AI agent improve by learning from its own past attempts, and both agree that what the agent learns should be kept and reused. They differ in how that accumulated knowledge is stored and fed back in on later runs, and IBM's argument is that this difference lands directly on the token bill.

**Why it matters**
Tokens are the running cost of an agent. Two methods can reach similar quality while one of them re-reads a much larger pile of accumulated context on every single step, so choosing between them is a budget decision as much as a research one — and it is the kind of cost that only becomes visible at scale.

Source: [Hugging Face ↗](https://huggingface.co/blog/ibm-research/altk-evolve-sldd)

### Postgres Hands Analytics Queries Off to ClickHouse

**What happened**
pg_clickhouse v0.10 adds subquery pushdown. Instead of pulling raw rows back into PostgreSQL and filtering them there, it sends more of the query down to ClickHouse — a database built for scanning large columns of data — and only brings back the result. ClickHouse reports up to 1000x faster queries on TPC-H, a standard analytics benchmark.

**Why it matters**
Plenty of companies keep their operational data in Postgres and then struggle when someone wants a report across all of it. Pushing the heavy part of the query to a system designed for it, without moving the data or changing the application, is the cheapest version of that fix.

Source: [ClickHouse ↗](https://clickhouse.com/blog/pg_clickhouse-whats-new-july-2026)

---
**Fun fact:** Horseshoe crab blood is bright blue — and still used to test vaccines for contamination.

*Daily tech digest for curious professionals. AI news that affects your work.*