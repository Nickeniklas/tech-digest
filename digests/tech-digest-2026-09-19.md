# Daily Tech Digest — Saturday, September 19 2026

> Google's Gemini was reportedly used to break into three companies — the first known case of a major AI model doing real damage in a real attack.

---
## Google's Gemini was reportedly used to hack three companies

**What happened**
According to a Wall Street Journal report relayed by Reuters, Google's Gemini model was used to break into three companies — described as the first known case of Google's AI being turned on real targets rather than test systems. It is the clearest sign yet that the same models people use for everyday work can be pointed at someone else's network.

**What this means**
Security teams have warned about this for two years; it has now moved from theory to an incident with named victims. If your organisation is writing an AI policy, the question is no longer only what staff might leak into a chatbot, but what an attacker can do with the same tools — and IT, legal, and compliance will all be asked about it.

Source: [Reuters ↗](https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/)

---
## Quick Hits

### Alibaba released a free medical AI that screens for cancer and ~150 other conditions

Alibaba open-sourced a medical model it says can detect cancer and close to 150 other conditions, meaning any hospital or researcher can download and run it rather than paying for access. Open-sourcing a diagnostic model is unusual — most stay locked inside the company that built them. For health systems outside wealthy countries, price is often the barrier, not the technology.

Source: [South China Morning Post ↗](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions)

### Cloudflare found another 100TB of memory it wasn't using

Cloudflare published how it cut a further 100 terabytes of memory from its servers, following an earlier round that saved the same amount — not by buying hardware, but by changing the maths behind how data is stored. It is a good reminder that a lot of infrastructure cost is waste nobody has looked at yet. The same logic applies to the storage and licences your team quietly keeps paying for.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)

### OpenAI used its own models to help design a chip

IEEE Spectrum detailed how OpenAI put its own language models to work designing Jalapeño, its in-house chip. Chip design is one of the slowest, most expensive engineering jobs there is, and this is one of the first concrete accounts of AI being used on the real thing rather than a demo. Expect the same argument — AI shortening specialist work — to arrive in your industry next.

Source: [IEEE Spectrum ↗](https://spectrum.ieee.org/llms-for-chip-design)

### Tiny models, measured in megabytes, are catching up

Cactus released Needle 3, a set of automation models between 8 and 29 megabytes that it claims match DeepSeek V4 Flash on the tasks they are built for. For scale, that is smaller than a few photos — small enough to sit on a phone with no internet connection. If it holds up, the assistant features in everyday apps stop needing a round trip to someone else's server.

Source: [Cactus Compute ↗](https://cactuscompute.com/needle)

---
## Under the Hood

### AUTOMATIC1111, rebuilt as a drag-and-drop canvas

**What happened**
Hugging Face rebuilt AUTOMATIC1111 — the interface most people used for local image generation — on top of Gradio Workflow, turning its stack of tabs into a node canvas. Text-to-image, hi-res fix, image-to-image, inpainting masks, upscaling, background removal and image-to-video are all nodes you wire together, and an LLM node can write the prompt for you. Every output is also exposed as an API.

**Why it matters**
The interesting part is not the visuals but the plumbing: a workflow built by dragging boxes around is immediately callable as an endpoint, so a designer's experiment becomes something a developer can automate without rewriting it. Models can run on Hugging Face or on your own GPU.

Source: [Hugging Face ↗](https://huggingface.co/blog/gradio-workflow-1111)

### 200+ WebGPU kernels for running models in the browser

**What happened**
Hugging Face released @huggingface/kernels, a library of more than 200 WebGPU kernels — the low-level routines that do the actual arithmetic of a model — written to run in a browser tab. Until now, browser-based inference mostly meant accepting whatever performance the framework gave you.

**Why it matters**
Kernels are where most of the speed in AI comes from, and hand-written ones for the browser have been scarce. With a catalogue this size, a model running locally on a laptop's graphics card becomes a realistic option for apps that cannot send data to a server — which is most apps handling client, patient, or student records.

Source: [Hugging Face ↗](https://huggingface.co/blog/webgpu-kernels)

---
**Fun fact:** Scientists have just described the first new cat species discovered in 100 years.

*Daily tech digest for curious professionals. AI news that affects your work.*