# Daily Tech Digest — Wednesday, September 2 2026

> Anthropic put out two new models today, Firefox finally got an ad blocker on iPhones, and the FBI is looking into a service that was selling 153 million driver's licenses.

---
## Anthropic Releases Claude Fable 5.1 and Mythos 5.1

**What happened**
Anthropic released two new models, Claude Fable 5.1 and Claude Mythos 5.1, aimed at coding and knowledge work. The company says their research abilities are an early sign of how these models will start contributing to scientific work.

**What this means**
Knowledge work is the stated target here, not just code — so if you draft, research, analyse or summarise for a living, this is the part of the product line meant for you. It is worth checking which model your tools actually use before assuming you have the newest one.

Source: [Anthropic ↗](https://www.anthropic.com/claude-fable-and-mythos-5-1)

---
## Quick Hits

### The FBI Is Investigating a Service That Sold 153 Million Driver's Licenses

Brian Krebs reports the FBI is probing a service that was selling data from more than 153 million driver's licenses. That is a scale where the question is less whether your details were in it and more what anyone can do with them once they are out.

Source: [Krebs on Security ↗](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)

### Firefox on iOS Now Has an Ad Blocker

Mozilla has shipped a built-in ad blocker for Firefox on iPhone and iPad. Apple's rules make ad blocking on iOS harder than on desktop, so having it built into the browser rather than bolted on as a separate app is the practical part.

Source: [Mozilla Blog ↗](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/)

### World Labs Published Atlas, a Model That Reasons About Space

World Labs released Atlas, which it describes as a world model for spatial intelligence — a system built to understand three-dimensional space rather than text. If it works as described, the eventual payoff is in robotics, architecture, and anything where software needs a sense of where things physically are.

Source: [World Labs ↗](https://www.worldlabs.ai/blog/atlas)

### The ChatGPT Desktop App Ships With a Whole Office Suite Inside It

Simon Willison found that OpenAI's ChatGPT/Codex app bundles a complete copy of LibreOffice, the free office suite. It is a reminder that AI apps are increasingly shipping other software inside themselves so the assistant can open and edit your files locally rather than uploading them.

Source: [Simon Willison ↗](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)

---
## Under the Hood

### Hugging Face Released 200+ WebGPU Kernels for Running AI in the Browser

**What happened**
Hugging Face published @huggingface/kernels, a library of more than 200 WebGPU kernels. A kernel is a small program that runs directly on your graphics card; WebGPU is the browser standard that lets a web page use that hardware. The kernels are distributed as repositories on the Hugging Face Hub, so a page can pull down the one it needs at runtime rather than shipping every variant.

**Why it matters**
Browser-based inference has been the slow path compared with running a model natively. Hand-tuned kernels are most of the gap. If you build web tools, this is what makes it plausible to run a model in the tab instead of sending user data to a server.

Source: [Hugging Face ↗](https://huggingface.co/blog/webgpu-kernels)

### Running a 104GB Model on a Mac With 48GB of Memory

**What happened**
A developer posted slotstream, a project that runs Qwen3.8-Flash-Next — a model that takes about 104GB — on a Mac with 48GB of memory, at roughly 12 tokens per second. The usual assumption is that a model has to fit in memory to run at all; this works around that limit rather than requiring the full model to be resident.

**Why it matters**
The ceiling on what you can run locally has been the amount of RAM you bought. Approaches like this move that ceiling, which matters if you want to keep sensitive material on your own machine instead of sending it to an API. Twelve tokens per second is slow — usable for a batch job, not for a live conversation.

Source: [GitHub ↗](https://github.com/carloslfu/slotstream)

---
**Fun fact:** Laurie Anderson's next manuscript will be sealed in Oslo until 2114 — nobody alive today gets to read it.

*Daily tech digest for curious professionals. AI news that affects your work.*