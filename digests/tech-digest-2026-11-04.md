# Daily Tech Digest — Wednesday, November 4 2026

> AI is learning to make slides that actually look like your company's, not like every other AI-made deck.

---
## IBM's Palette teaches a small AI model to build decks in your own design style

**What happened**
IBM Research introduced Palette, a small AI model trained to build slide decks that follow a specific company template rather than a generic look. The team's starting point: ask a frontier model for ten decks and they start to look alike, with the same tasteful defaults and a faint 'AI-generated' style.

**What this means**
If you make presentations for clients or leadership, the hard part is rarely the content; it is matching the brand. Tools built like this could give marketers, consultants and teachers first drafts that already use their own fonts, layouts and colours.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/ibm-research/palette-deck-building)

---
## Quick Hits

### Postman accused of quietly installing AI plugins

A widely discussed bug report on GitHub says the Postman app, a popular tool for testing how software services talk to each other, silently auto-installs AI plugins and attempts to share all of a user's API data. If your team uses Postman, it is worth asking IT to check its settings before sensitive data leaves the building.

Source: [GitHub (Postman issue tracker) ↗](https://github.com/postmanlabs/postman-app-support/issues/14370)

### Figma is training an AI model that speaks its language

Figma says it is training an editing model that is 'Figma-fluent' — built to understand and change designs inside Figma itself rather than describe them from the outside. For designers, that points toward AI edits that respect your existing layers and components.

Source: [Figma Blog ↗](https://www.figma.com/blog/training-a-figma-fluent-editing-model/)

### AI is driving a comeback for magnetic tape

Fujifilm plans to boost its tape production fivefold as AI fuels demand for long-term data archiving, Ars Technica reports. Tape is old technology, but it remains one of the cheapest ways to store huge amounts of data for years.

Source: [Ars Technica ↗](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)

### Safari adds Adaptive Dark Mode

Apple's WebKit team introduced Adaptive Dark Mode in Safari 27.3, which can show websites in dark colours even when they were not designed with a dark version. If you read on your phone at night, more of the web should now be easier on your eyes.

Source: [WebKit Blog ↗](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

---
## Under the Hood

### StateBench: can AI keep track of what changes in a long document?

**What happened**
The Allen Institute for AI introduced StateBench, a benchmark for long-context state tracking — measuring how well language models keep track of information about people, things and places as it changes over the course of a long document.

**Why it matters**
Contracts, case files and long reports constantly update facts ('the deadline moved', 'the tenant left'). A model that loses track of the latest state gives confident but outdated answers, so tests like this help show which tools you can trust with long documents.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/statebench)

### CWE-bench v2 opens 100 public cybersecurity tasks for AI agents

**What happened**
Collinear AI released CWE-bench v2, a test of frontier AI models' cyber capabilities. It opens up a public set of 100 tasks that anyone can run; in each, an AI agent gets a copy of a real open-source codebase to work on.

**Why it matters**
As AI agents get better at finding software flaws, defenders need open, repeatable ways to measure that skill. A public task set lets researchers and security teams compare models on the same ground instead of relying on vendor claims.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/cwe-bench)

---
**Fun fact:** Researchers have seen writing inside the scorched Herculaneum scroll PHerc. 306B for the first time in 2,000 years.

*Daily tech digest for curious professionals. AI news that affects your work.*