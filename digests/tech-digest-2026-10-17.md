# Daily Tech Digest — Saturday, October 17 2026

> New research suggests the tests used to measure AI progress miss most of what people actually do at work.

---
## AI benchmarks miss 90% of the work people actually do

**What happened**
Mercor mapped how US working hours are spent against the benchmarks AI labs use to measure their models, and found that 90% of working hours go to tasks those tests don't cover well.

**What this means**
When a company says its new model "beats" another, that score probably says little about your own job. The safest way to judge an AI tool is still to try it on your real tasks — drafting a lesson plan, reviewing a contract, planning a campaign.

Source: [Mercor ↗](https://www.mercor.com/research/labor-index/benchmark-map/)

---
## Quick Hits

### Waymo heads to Toronto

Waymo, the self-driving taxi company owned by Google's parent Alphabet, announced Toronto as a new city for its driverless cars. For people in other cities, it's a signal that driverless taxis are spreading beyond a handful of US test markets.

Source: [Waymo ↗](https://waymo.com/blog/2026/10/waymo-in-toronto/)

### Claude helps design more efficient quantum circuits

Anthropic published research on using Claude to design quantum circuits — the step-by-step instructions quantum computers run — that run more efficiently. It's another sign that AI is becoming a working tool for scientists, not just a writing assistant.

Source: [Anthropic ↗](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

### FLUX 3 Image Klein: a new image generator from Black Forest Labs

Black Forest Labs released FLUX 3 Image Klein, a new AI image model, and it is already available in Hugging Face's Diffusers library for anyone to run. If you make visuals for presentations or marketing, expect it to show up inside the design tools you already use.

Source: [Black Forest Labs ↗](https://bfl.ai/blog/flux-3-image-klein)

### Tiny magnetic robots deliver medicine inside a beating heart

Johns Hopkins researchers built wireless millirobots, steered by magnets from outside the body, that can carry medicine to the heart while it keeps beating. The approach could one day replace some invasive procedures.

Source: [Johns Hopkins University ↗](https://hub.jhu.edu/2026/10/12/magnetic-millirobots-cardiac-treatment/)

---
## Under the Hood

### Beam: a 501-billion-parameter open model you can run yourself

**What happened**
Reflection released Beam, an open model with 501 billion parameters (the internal settings a model learns during training). It uses a mixture-of-experts design — only part of the model switches on for each word — and supports long documents. Hugging Face's write-up covers benchmarks, hardware requirements, and fine-tuning recipes.

**Why it matters**
Beam is pitched as a model you can own outright: download it, customise it, and host it on your own hardware. It works with the standard open-source serving and training tools from day one, so teams can try it without rebuilding their setup.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/reflection-beam)

### Apple runs Meta's Muse Spark Open across Mac Studios

**What happened**
Previously covered on 2026-10-16: Meta released Muse Spark Open, a free-to-download model that handles text, images and audio. Since then, Apple's machine learning research team showed it running on Mac Studio computers using MLX, Apple's open-source framework, with the work split across multiple machines.

**Why it matters**
Large open models usually need expensive data-centre chips. Spreading one across a few desktop Macs gives small teams and researchers a way to run frontier-scale models privately, on hardware they can buy off the shelf.

Source: [Apple Machine Learning Research ↗](https://machinelearning.apple.com/research/mlx-distributed-inference)

---
**Fun fact:** Scientists have made a "super ice" 10 times stronger than normal ice — close to the strength of concrete.

*Daily tech digest for curious professionals. AI news that affects your work.*