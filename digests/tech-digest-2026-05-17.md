# Daily Tech Digest — Sunday, May 17 2026

> A free, open-source AI studio puts 200 models for generating images and video on your own server — no subscription, no data sharing.

---
## A Free, Self-Hosted AI Creative Studio Brings 200+ Models to Anyone With a Server

**What happened**
Open-Generative-AI launched on GitHub as an open-source, self-hosted alternative to commercial AI creative tools. It bundles over 200 AI models for generating images and video — including alternatives to Midjourney, Sora, Kling, and Veo — in a browser-based studio with no content restrictions and an MIT license.

**What this means**
If you produce visual content for work — presentations, marketing campaigns, social media, or client work — this gives you a free, private alternative to paid AI image services. Your prompts and generated content stay on your own server rather than passing through a third-party platform.

Source: [GitHub ↗](https://github.com/Anil-matcha/Open-Generative-AI)

---
## Quick Hits

### Private, On-Device AI Assistant Continues to Gain Traction on GitHub

Previously covered on 2026-05-12: OpenHuman — an AI assistant that runs entirely on your computer without sending data to a cloud — is still among GitHub's fastest-growing open-source projects days after launch. The sustained attention signals that privacy-focused AI tools are filling a real gap, particularly for professionals handling sensitive work.

Source: [GitHub ↗](https://github.com/tinyhumansai/openhuman)

### On-Device Multilingual Text-to-Speech Keeps Attracting Developers

Previously covered on 2026-05-14: Supertone's supertonic remains on GitHub's trending list — an on-device, multilingual text-to-speech tool with no internet requirement. For educators recording lesson audio, podcast producers, or marketers localizing content, the combination of speed and language support continues to draw attention.

Source: [GitHub ↗](https://github.com/supertone-inc/supertonic)

### WiFi-Based Presence and Vital Sign Detection Remains a Trending Topic

Previously covered on 2026-05-15: RuView — the tool that converts standard WiFi router signals into a sensor for detecting people's presence, movement, and vital signs — remains in GitHub's trending section. It requires no cameras or dedicated hardware, which is attracting interest from building managers, healthcare researchers, and privacy advocates alike.

Source: [GitHub ↗](https://github.com/ruvnet/RuView)

---
## Under the Hood

### Codegraph: Pre-Indexing Your Codebase to Cut Claude Code's Token Overhead

**What happened**
Codegraph builds a structured knowledge graph from your project's source code before any AI session begins. When Claude Code needs to locate a function, trace an import, or understand a dependency, it queries the pre-built index in one step rather than reading through files sequentially.

**Why it matters**
Claude Code's file-reading operations each consume tokens. On larger codebases, exploratory reads — searching for class definitions, tracing call chains — can account for a significant share of a session's token budget. Codegraph turns many sequential reads into a single indexed lookup, which reduces both API cost and session latency. The index is built and stored entirely locally; no code is transmitted externally.

Source: [GitHub ↗](https://github.com/colbymchenry/codegraph)

---
**Fun fact:** Two hundred AI models, one self-hosted install, zero monthly fees — if you're willing to run the server yourself.

*Daily tech digest for curious professionals. AI news that affects your work.*