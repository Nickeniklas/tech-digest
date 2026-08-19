# Daily Tech Digest — Wednesday, August 19 2026

> The memory chips inside your next laptop cost five times what they did last summer, and that bill is heading for everyone's hardware budget.

---
## Computer Memory Costs Five Times What It Did a Year Ago

**What happened**
Tom's Hardware reports that memory prices have climbed roughly 500% in twelve months — up to ten times the cheapest levels ever tracked. A 128GB kit of DDR5, the standard memory in current desktops and workstations, is now listed at $3,399.

**What this means**
Anything with memory in it — laptops, phones, servers, cloud instances — gets more expensive from here. If your team is planning a hardware refresh or budgeting for one, quotes from earlier this year are already out of date, and waiting is not obviously the cheaper move.

Source: [Tom's Hardware ↗](https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399)

---
## Quick Hits

### Apple Changes How Apps Work in the European Union

Apple published a set of changes for apps distributed in the EU. The details matter most to developers, but they shape what you can install on an iPhone in Europe and how you pay for it.

Source: [Apple Newsroom ↗](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/)

### Cursor Launches a GitHub Alternative

Cursor, the AI code editor, has launched Origin — its own service for storing and hosting code, the job GitHub does for most of the software industry. It is a move to own the whole workflow rather than just the editing part of it.

Source: [Cursor ↗](https://cursor.com/changelog/origin-code-hosting)

### Meta Releases an Open AI Model That Runs on Your Own Machine

Meta published Muse Glimmer, an open source model that handles both text and images, can carry out multi-step tasks, and runs locally instead of in someone else's data centre. Open releases like this are what let organisations use AI without sending their material to an outside vendor.

Source: [Hugging Face ↗](https://huggingface.co/blog/muse-glimmer)

### A 25-Year-Old Video Patent Expires, Clearing a Problem for Linux

A Brazilian patent covering video technology has run out, ending a long-standing legal complication for Linux. In practice it means open source systems can ship video playback support that was previously awkward to include.

Source: [XDA Developers ↗](https://www.xda-developers.com/25-year-old-brazilian-video-patent-expired-legal-headache-linux/)

---
## Under the Hood

### Search That Compares Every Word, Not Just the Whole Document

**What happened**
Sentence Transformers, one of the most widely used open source search libraries, now supports multi-vector — or "late interaction" — models. Instead of compressing a document into a single list of numbers, these models keep one list per token and score a query by matching each query token to its best counterpart in the document, an operation called MaxSim.

**Why it matters**
Late interaction retrieval is more accurate than single-vector search, particularly on documents where a few specific terms carry the meaning — contracts, technical manuals, medical notes. The trade-off is storage and compute, since you are keeping and comparing far more vectors per document. Having it built into Sentence Transformers means teams can test whether that trade is worth it without building the plumbing first.

Source: [Hugging Face ↗](https://huggingface.co/blog/multi-vector-encoder)

### How Much Memory an AI Agent Needs Depends on How Capable It Already Is

**What happened**
IBM Research tested how much accumulated memory an AI agent actually needs, comparing three configurations across models of different strength. More memory did not reliably mean better results, and the cheapest memory strategy was frequently the best performing one.

**Why it matters**
Agent memory is usually treated as something to hoard — keep everything, in case it turns out useful. This argues it should be calibrated instead: a stronger model needs less scaffolding around it, and a weaker one may not benefit from more of it. That is a direct cost lever for anyone running agents at scale, because every remembered token is paid for again on every call.

Source: [Hugging Face ↗](https://huggingface.co/blog/ibm-research/altk-evolve-hmm)

---
**Fun fact:** A macOS desktop toy renders a 3D fruit fly driven by the real FlyWire map of its brain.

*Daily tech digest for curious professionals. AI news that affects your work.*