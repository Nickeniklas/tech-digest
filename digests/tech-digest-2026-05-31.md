# Daily Tech Digest — Sunday, May 31 2026

> A free tool turns your existing WiFi router into a room monitor that tracks presence and vital signs — no cameras, no microphones, no new hardware.

---
## Your WiFi Router Can Now Monitor Rooms Without Any Cameras

**What happened**
A developer published RuView, a free open-source tool that converts standard WiFi signals into real-time spatial intelligence — detecting people's presence, movement, and vital signs like breathing patterns, all without installing a single camera or sensor.

**What this means**
For facilities managers and HR teams, this creates possibilities for occupancy tracking and workplace safety monitoring without video surveillance infrastructure. For everyone else, it's a striking reminder that physical privacy may depend less on cameras than on the wireless signals already filling your home or office.

Source: [GitHub ↗](https://github.com/ruvnet/RuView)

---
## Quick Hits

### A New Open-Source Voice Model Generates Realistic Speech in Any Language

OpenBMB released VoxCPM2, a free speech model built for high-fidelity multilingual voice generation, voice cloning, and long narrations with multiple speakers. It skips the tokenization step that limits most multilingual voice tools, producing more natural results. Content creators, educators, and podcasters working across languages now have a self-hostable option.

Source: [GitHub ↗](https://github.com/OpenBMB/VoxCPM)

### A Free Tool Automates Video Uploads to TikTok, YouTube, and More

A developer released social-auto-upload, an open-source tool that posts videos to multiple platforms — TikTok, YouTube, Bilibili, and others — automatically from a single workflow. For marketing teams managing multi-platform content, it removes the repetitive manual upload step.

Source: [GitHub ↗](https://github.com/dreammis/social-auto-upload)

### A Free 9-Week Data Engineering Course Is Available to Anyone Right Now

DataTalksClub published a complete, self-paced course on building production-ready data pipelines — the infrastructure behind dashboards, reports, and analytics systems. No tuition, no subscription. The next formal cohort begins January 2026, but all materials are publicly available now.

Source: [GitHub ↗](https://github.com/DataTalksClub/data-engineering-zoomcamp)

### A Step-by-Step Guide to Building Your Own Language Model Is Trending

A new GitHub project walks through the full process of training a language model from scratch — from sourcing data to generating text — in a deliberately plain, accessible way. It's aimed at curious learners who want to understand how models like GPT actually work, not just use them.

Source: [GitHub ↗](https://github.com/FareedKhan-dev/train-llm-from-scratch)

---
## Under the Hood

### VoxCPM2: What 'Tokenizer-Free' Actually Means for Voice AI

**What happened**
The OpenBMB team released VoxCPM2, a speech synthesis model that removes the tokenizer — the step where most voice AI systems convert audio into discrete chunks before processing. Eliminating that step lets the model handle multilingual speech more naturally, clone voices with higher fidelity, and sustain quality across long narrations without the audio artifacts tokenized systems typically introduce.

**Why it matters**
Traditional TTS models train separate per-language systems or sacrifice quality when switching languages mid-sentence. A token-free architecture processes audio as a continuous signal, which is closer to how human hearing works. This matters for audiobook production, real-time translation, and multi-speaker podcast generation. It's fully open-source and self-hostable — no API costs.

Source: [GitHub ↗](https://github.com/OpenBMB/VoxCPM)

---
**Fun fact:** RuView detects breathing through walls using the same WiFi signal your laptop uses for email.

*Daily tech digest for curious professionals. AI news that affects your work.*