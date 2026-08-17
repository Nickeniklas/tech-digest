# Daily Tech Digest — Monday, August 17 2026

> Firefox now blocks ads on the iPhone without any setup, and Anthropic has started publishing the standing instructions it gives Claude.

---
## Firefox on the iPhone Now Blocks Ads Out of the Box

**What happened**
Previously covered on 2026-08-15: Firefox became the last major browser where the ad blocker uBlock Origin still works in full. Since then, Mozilla has added ad blocking directly into Firefox for iOS — no extension, no separate app, nothing to configure.

**What this means**
Ad blocking on the iPhone has until now meant installing something extra, so most people never did it. Marketers should expect a further slice of mobile readers who simply never see display ads, and anyone reading long articles on a phone gets a quieter page.

Source: [Mozilla Support ↗](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios)

---
## Quick Hits

### Anthropic Publishes the Instructions It Gives Claude

Anthropic now lists Claude's system prompts — the standing instructions the assistant is given before you type anything — in its public release notes. If you have ever wondered why an AI assistant refuses a request, formats answers a certain way, or hedges on some topics, a good part of the answer is now readable.

Source: [Anthropic Docs ↗](https://platform.claude.com/docs/en/release-notes/system-prompts)

### A Resale Market Has Grown Up Around AI Credits

A report describes the brokers who buy and resell access to AI models — the credits companies pay for by the word. It is a reminder that the price you pay for an AI tool is not always the price the provider charges, and that some cheap offers are somebody else's leftover capacity.

Source: [Vectoral ↗](https://vectoral.com/blog/who-are-the-token-brokers)

### A New Open Model Is Strong but Talks Itself in Circles

Developer Simon Willison put Qwen 3.8 27B through its paces and rates it excellent, with one catch: left alone, it overthinks simple questions. It is a useful reminder that raw model quality and everyday usefulness are not the same thing.

Source: [Simon Willison ↗](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)

### Keyword Lists Were Used to Cancel Billions in Research Grants

Higher Ed Dive obtained the federal keyword lists used to screen research grants, and traces how matching a word on a list led to billions of dollars in cancelled funding. If your work touches grant applications or public-sector procurement, it is worth seeing how mechanical the filtering was.

Source: [Higher Ed Dive ↗](https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/)

---
## Under the Hood

### A Step-by-Step Timeline of an AI Lab Break-In

**What happened**
Hugging Face published a technical reconstruction of the July 2026 intrusion at a frontier AI lab, laying out the incident as a timeline of how the attack unfolded around the lab's AI agents rather than as a summary after the fact.

**Why it matters**
Agents are software that acts on your behalf — reading files, calling tools, making requests — so an attacker who steers an agent inherits whatever that agent is allowed to do. Published timelines are how the rest of the industry learns what the failure actually looked like instead of guessing.

Source: [Hugging Face ↗](https://huggingface.co/blog/agent-intrusion-technical-timeline)

### Zero-Knowledge Proofs, Explained Briefly

**What happened**
A short walkthrough of zero-knowledge proofs: a method for proving a statement is true without handing over the information behind it. The post builds the idea up from the basics rather than starting from the mathematics.

**Why it matters**
This is the machinery behind age checks that do not require uploading an ID, and payment checks that do not expose a balance. As identity verification rules spread, it is the difference between proving something about yourself and surrendering the underlying data.

Source: [Max Bernstein ↗](https://bernsteinbear.com/blog/zkp/)

---
**Fun fact:** Someone got a working telnet bulletin board running on a Casio calculator.

*Daily tech digest for curious professionals. AI news that affects your work.*