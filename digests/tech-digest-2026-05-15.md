# Daily Tech Digest — Friday, May 15 2026

> Your WiFi router can already detect your heartbeat — a new open-source tool makes that power accessible to anyone.

---
## WiFi Signals Can Now Monitor Vital Signs and Detect Presence — No Camera Required

**What happened**
A developer released RuView, a tool that converts ordinary WiFi router signals into a real-time sensor for detecting people's presence, monitoring vital signs, and mapping spatial movement — without any cameras, microphones, or dedicated hardware.

**What this means**
Any room with a standard WiFi router could become a monitoring environment. For healthcare and elder care managers, this means tracking patient movement and breathing without intrusive cameras. For office and facilities teams, it means occupancy sensing that never captures video. The same capability also raises new privacy questions about what WiFi routers already know about the people around them.

Source: [GitHub Trending ↗](https://github.com/ruvnet/RuView)

---
## Quick Hits

### Y Combinator's CEO Published His Personal AI Coding Setup

Garry Tan — CEO of Y Combinator, the startup accelerator behind Airbnb, Dropbox, and Stripe — published his exact Claude Code configuration on GitHub. The setup includes 23 pre-built AI tools, each assigned a specific professional role: CEO, Designer, Engineering Manager, Release Manager, and more. It's a ready-to-use template for anyone who wants structured, role-specific AI workflows instead of just prompting a generic assistant.

Source: [GitHub Trending ↗](https://github.com/garrytan/gstack)

### Kronos: An AI Model Trained on the Language of Financial Markets

Researchers published Kronos, a foundation model built specifically on financial market data — not just news, but the notation, patterns, and communication formats that traders and analysts use daily. General AI models handle finance as one topic among thousands; Kronos was designed from the ground up for market language. Finance professionals may find it more reliable than general-purpose models for market data, earnings reports, or financial modeling tasks.

Source: [GitHub Trending ↗](https://github.com/shiyu-coder/Kronos)

### NVIDIA Released AI Blueprints for Searching and Summarizing Video

NVIDIA published reference architectures for building AI systems that can automatically search through video content and generate summaries. The blueprints target businesses that produce or manage large volumes of video — security teams, broadcasters, manufacturers, and retailers. Developers can use them as GPU-accelerated starting points rather than building video AI pipelines from scratch.

Source: [GitHub Trending ↗](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)

---
## Under the Hood

### How Garry Tan's gstack Structures AI Into 23 Specialized Roles

**What happened**
The gstack repository packages 23 Claude Code skills — each a plain-text instruction file defining a professional persona with specific goals, constraints, and decision-making priorities. When invoked, each tool loads its role definition as context so Claude responds from that perspective: the CEO tool focuses on trade-offs and strategy; the QA tool focuses on edge cases and breakage; the Doc Engineer focuses on accuracy and completeness.

**Why it matters**
The pattern separates concerns that generic AI prompting tends to muddle. When you ask a single AI assistant to write code and then review it, it tends to approve its own work. Giving each task its own role definition — with different success criteria — produces outputs that are less self-confirming. The approach is reproducible: you fork the repo, edit the plain-text role files, and the specialized behavior follows without any code changes.

Source: [GitHub Trending ↗](https://github.com/garrytan/gstack)

---
**Fun fact:** Garry Tan's AI setup assigns Claude 23 job titles at once — including CEO, Designer, and QA.

*Daily tech digest for curious professionals. AI news that affects your work.*