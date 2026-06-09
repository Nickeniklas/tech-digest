# Daily Tech Digest — Tuesday, June 9 2026

> Google just published an official library of AI agent skills for its own products — meaning AI tools can now operate Google Docs, Gmail, and Sheets on your behalf, out of the box.

---
## Google Publishes Official AI Agent Skills for Its Own Products

**What happened**
Google released a public repository of agent skills — pre-built instructions that let AI agents understand and work with Google products like Docs, Sheets, Gmail, and Drive without custom setup. Any AI tool that supports agent skills can now pull these in directly.

**What this means**
If you use AI tools at work, this means they'll soon be able to handle Google Workspace tasks — drafting in Docs, crunching numbers in Sheets, replying in Gmail — with far less setup. Teachers, marketers, and lawyers who rely on Google's tools daily are the obvious first beneficiaries.

Source: [GitHub ↗](https://github.com/google/skills)

---
## Quick Hits

### 100+ AI Skills for Product Managers, Free to Download

A new open-source collection called PM Skills packs over 100 reusable AI instructions for every phase of product work — from early discovery through launch and growth. Drop them into any AI coding tool and they guide it through PM-specific tasks. It's a sign that curated skill packs are becoming the fastest way to get useful AI assistance without starting from scratch.

Source: [GitHub ↗](https://github.com/phuryn/pm-skills)

### A Free Tool Tells You Which AI Model Runs Best on Your Hardware

A command-line tool called whichllm benchmarks local AI models against your actual hardware and ranks them by real performance — not just model size. Run one command and it tells you which open-source model will run fastest on your machine. This is useful for anyone who wants to run AI privately without sending data to the cloud.

Source: [GitHub ↗](https://github.com/Andyyyy64/whichllm)

### Goose: An Open-Source AI Agent That Can Actually Run Your Computer

Goose is a free AI agent that goes well beyond suggesting code — it can install software, run tests, edit files, and execute tasks on your machine, all from a single interface. It works with any large language model, so you're not locked into one provider. Think of it as a capable AI assistant that acts on your computer instead of just answering questions.

Source: [GitHub ↗](https://github.com/aaif-goose/goose)

---
## Under the Hood

### A Visual Guide to Claude Code With Copy-Paste Templates

**What happened**
Developer luongnv89 published claude-howto, a free repository of visual examples and ready-to-use templates for Claude Code — Anthropic's AI coding assistant. It covers basic concepts through advanced multi-agent setups, with practical templates organized by concept rather than documentation pages.

**Why it matters**
For developers ramping up on Claude Code, this is a shortcut through the learning curve. Instead of reading docs linearly, you get working templates at every level — from simple file tasks to coordinating multiple AI agents. It's the kind of resource that turns hours of experimentation into minutes.

```python
# Summarize a file
claude "Read main.py and write a 2-sentence summary"

# Code review
claude "Review utils.py for potential bugs and suggest fixes"

# Multi-step agent task
claude --agent "Review all .py files and list any functions over 50 lines"
```

Source: [GitHub ↗](https://github.com/luongnv89/claude-howto)

### Roboflow Supervision: A Free Reusable Toolkit for AI Computer Vision

**What happened**
Roboflow's supervision library — a free, reusable set of computer vision building blocks — is trending again on GitHub. It handles object detection, tracking across video frames, annotation drawing, and dataset management so developers don't rebuild these pieces every time. It works alongside major models including YOLO and SAM.

**Why it matters**
Computer vision is the technology behind security cameras, retail analytics, document scanning, and medical imaging. Supervision lowers the barrier for developers who don't specialize in vision, making it easier to build products that can see and interpret the physical world without starting from scratch each time.

```python
import supervision as sv
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("image.jpg")[0]
detections = sv.Detections.from_ultralytics(results)
annotator = sv.BoxAnnotator()
annotated = annotator.annotate(scene=image, detections=detections)
```

Source: [GitHub ↗](https://github.com/roboflow/supervision)

---
**Fun fact:** Three separate AI 'skills' libraries are trending on GitHub today — from Google, product managers, and an independent developer.

*Daily tech digest for curious professionals. AI news that affects your work.*