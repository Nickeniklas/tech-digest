# Daily Tech Digest — Friday, October 23 2026

> A free map of the whole planet built by AI, a fee for streaming games you already own, and new research on letting AI check that software actually works.

---
## OlmoEarth v1.3 maps the whole planet with AI — and you can explore it in your browser

**What happened**
The Allen Institute for AI released OlmoEarth v1.3, an AI model that turns satellite imagery into compact summaries of what's on the ground. Alongside it, they published ready-made yearly summaries for the entire planet at 10-metre detail, plus a free browser tool for exploring and customising maps built from them.

**What this means**
You no longer need a data science team to ask questions of satellite data. Urban planners, journalists, researchers, NGOs and teachers can start from planet-wide maps that are already computed, rather than processing raw imagery themselves.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/olmoearth-v1-3)

---
## Quick Hits

### Xbox wants to charge per hour to stream games you already bought

Ars Technica reports that Xbox plans to charge 24 to 40 cents per hour to stream games from the cloud, including games you've already paid for. If you play this way, an evening of gaming could start to carry a running meter.

Source: [Ars Technica ↗](https://arstechnica.com/gaming/2026/10/xbox-wants-you-to-pay-24-to-40-cents-per-hour-to-stream-games-you-already-bought/)

### Quad9 is leaving France

Quad9, a free non-profit service that translates website names into addresses and blocks known malicious sites, announced it is exiting France. If your organisation or home network uses Quad9 for protection, check whether you're affected and what to switch to.

Source: [Quad9 ↗](https://quad9.net/news/blog/au-revoir-france/)

### eMudhra quits the website certificate business

Previously covered on 2026-10-21: a report described a compromise of one of eMudhra's certificate authorities, the organisations that vouch for websites as secure. Since then, eMudhra has announced it is exiting the global SSL/TLS certificate business entirely. Sites that rely on its certificates will need to move to another provider.

Source: [eMudhra ↗](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)

### Anthropic: AI is making mathematically proven software practical

Anthropic published research arguing that AI models are making formal verification — mathematically proving that software does exactly what it should — feasible at a much larger scale. Until now this level of checking was so slow and expensive it was reserved for things like aircraft and chip design.

Source: [Anthropic ↗](https://www.anthropic.com/research/formal-verification)

---
## Under the Hood

### GitHub has copied 99.99999% of its repositories to Azure

**What happened**
GitHub says it has moved a copy of 99.99999% of its repositories to Microsoft's Azure cloud. Its engineering post explains how it plans to bring over the rest using per-reference quorums — agreement between servers on every single branch update — and how object storage lets reading code scale separately from writing it.

**Why it matters**
GitHub frames this as infrastructure for 'agent scale': AI coding agents create far more traffic than humans do. For engineering leaders, it's a sign of the load AI agents are expected to put on the tools your teams depend on.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/)

### Rebuilding GitHub's star history: from 2,500 requests to 24

**What happened**
GitHub launched a new API that shows how a project's star count changed over time. Building that chart used to take around 2,500 requests; the new approach needs 24 and no longer returns the identities of the individual people who starred a project.

**Why it matters**
It's a clear example of a privacy and performance win at once: aggregate trends instead of personal data, with bounded database work. Useful reading for anyone designing analytics features.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/)

---
**Fun fact:** A startup just ran a test drawing energy from an underwater volcano.

*Daily tech digest for curious professionals. AI news that affects your work.*