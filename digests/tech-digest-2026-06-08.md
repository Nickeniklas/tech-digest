# Daily Tech Digest — Monday, June 8 2026

> Today's most interesting release is a computer built to keep working when the internet doesn't — plus a tool that teaches AI bots better taste.

---
## A New Offline AI Computer Wants to Keep You Informed When the Internet Doesn't

**What happened**
A developer released Project N.O.M.A.D, a self-contained, portable device that bundles offline reference tools, survival knowledge, and AI assistance into one box — built to keep working without any internet connection.

**What this means**
Most AI tools you use every day depend on a constant link to a company's servers. This project is part of a small but growing push toward AI that runs entirely on your own hardware — handy for fieldwork, travel, remote teams, or anyone who'd simply rather keep their data off someone else's cloud.

Source: [GitHub ↗](https://github.com/Crosstalk-Solutions/project-nomad)

---
## Quick Hits

### An AI Skill That Teaches Other AI Tools 'Good Taste'

A developer released Taste-Skill, a small add-on you can drop into AI coding tools to stop them from churning out bland, generic-looking results. It works by giving the AI a clearer sense of design sensibility before it starts generating anything.

Source: [GitHub ↗](https://github.com/Leonxlnx/taste-skill)

### The Quiet Engine Behind Most Local AI Chatbots Is Trending Again

llama.cpp, the open-source software that lets AI language models run directly on your laptop or phone instead of in the cloud, is back near the top of GitHub's trending list. It's the engine quietly powering many of the privacy-focused AI apps you may already be using.

Source: [GitHub ↗](https://github.com/ggml-org/llama.cpp)

### A New Desktop App Turns Your Notes Into a Personal Knowledge Base

Tolaria is a new desktop application for organizing markdown notes into a connected knowledge base — the kind of system researchers and writers use to link related ideas together over time. It's free and open-source.

Source: [GitHub ↗](https://github.com/refactoringhq/tolaria)

### A Free Tool Shows How Much a Phone Number Can Reveal About You

GhostTrack is an open-source tool that demonstrates how publicly available information can be pieced together to trace a phone number or general location. It's built for researchers and security professionals, but it's also a useful reminder of how much can be learned from small digital traces.

Source: [GitHub ↗](https://github.com/HunxByts/GhostTrack)

---
## Under the Hood

### Microsoft Builds Durable Workflows Directly Into PostgreSQL

**What happened**
Microsoft published pg_durable, an open-source extension that lets the popular PostgreSQL database track long-running workflows on its own — so if a process is interrupted partway through, it can pick up exactly where it left off instead of restarting from scratch or losing data.

**Why it matters**
Plenty of behind-the-scenes business processes — order processing, approval chains, scheduled jobs — depend on this kind of reliability. Normally, teams bolt on a separate workflow service to get it; folding that capability into a database many companies already run can mean less complexity and fewer moving parts to maintain.

Source: [GitHub ↗](https://github.com/microsoft/pg_durable)

### A New Rust-Based Search Index Aims to Make AI Search Faster

**What happened**
Developer Ryan Codrai released Turbovec, an open-source vector index — the kind of system AI search tools use to quickly find related pieces of information — built in Rust on top of a project called TurboQuant, with ready-to-use Python bindings.

**Why it matters**
Vector search underpins everything from AI chatbots that search your documents to recommendation engines. A leaner, faster index like this could let smaller teams build those features without heavyweight infrastructure — useful for developers building in-house AI search tools.

Source: [GitHub ↗](https://github.com/RyanCodrai/turbovec)

---
**Fun fact:** Yes, you can now download 'good taste' for your AI assistant — as a GitHub repository.

*Daily tech digest for curious professionals. AI news that affects your work.*