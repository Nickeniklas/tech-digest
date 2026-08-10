# Daily Tech Digest — Monday, August 10 2026

> Anthropic put out a new top-tier Claude model at half the price of its most capable one — the clearest sign yet that the good models are getting cheaper, not just better.

---
## Anthropic Releases Claude Opus 5

**What happened**
Anthropic released Claude Opus 5, an update to its Opus tier of models, available today. The company says it comes close to the intelligence of Claude Fable 5, its most capable model, at half the price, with the biggest gains in long-running agent work, coding, and professional tasks.

**What this means**
The practical story here is price, not capability: near-top-tier work at half the cost changes what a firm can afford to run all day rather than once in a while. If your team uses an AI assistant for drafting, review, or research, the version you get is likely to quietly improve over the next few weeks without you doing anything.

Source: [Anthropic ↗](https://www.anthropic.com/news/claude-opus-5)

---
## Quick Hits

### A Japanese Court Overturned Red's RAW Video Patent

Panasonic won a case in Japan invalidating Red's patent on compressed RAW video recording — a patent Apple, Sony and Nikon had all failed to overturn. RAW is the uncompressed-quality format professional video editors prefer, and Red's patent has shaped which cameras could offer it. Expect the feature to appear in more cameras, at lower prices.

Source: [DPReview ↗](https://www.dpreview.com/news/panasonic-did-what-apple-sony-and-nikon-couldnt-overturn-a-red-raw-video-patent/)

### A Working Method for Learning Hard Things With an AI Model

A developer wrote up the routine they use to learn unfamiliar technical subjects with a language model: not asking it for answers, but using it to test whether their own explanation holds up. It is a useful counterweight to the standard advice, and the method transfers to any field where you have to get up to speed fast.

Source: [Laurentiu Gabriel ↗](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/)

### Windows 11's Weather App Uses More Than a Gigabyte of Memory

Testing found the small weather widget built into Windows 11 holding over 1 GB of RAM — more than many full applications. If your work laptop feels slow for no obvious reason, background system apps are a fair place to look before you blame the machine.

Source: [Notebookcheck ↗](https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html)

### Turn Satellite Imagery Into a Paper Globe You Fold Yourself

A small web tool takes satellite imagery and lays it out as a printable net you cut and fold into a globe. It costs nothing and needs no account, and it is an easy classroom or desk project for anyone who teaches geography or just likes making things by hand.

Source: [Folding Globes ↗](https://foldingglobes.com/)

---
## Under the Hood

### 4-Bit Image Generation Lands in Diffusers

**What happened**
Hugging Face added Nunchaku 4-bit inference to Diffusers, the standard Python library for running image-generation models. Quantisation stores each of a model's numeric weights in fewer bits — dropping from the usual 16 bits to 4 cuts the memory the weights occupy by roughly four times, at some cost in output fidelity.

**Why it matters**
Memory, not raw speed, is usually what stops a large image model from running on a consumer graphics card. Making 4-bit a first-class option in the mainstream library means fewer people have to assemble a custom stack to run these models locally.

Source: [Hugging Face ↗](https://huggingface.co/blog/nunchaku-diffusers)

### Idle GPUs Are the New Grounded Aircraft

**What happened**
A piece on GPU management argues that AI infrastructure should be measured the way airlines measure fleets: the expensive asset only earns while it is in use, so utilisation matters more than how many you own. The comparison is a reasonable frame for why GPU scheduling has become its own discipline.

**Why it matters**
If you are budgeting for AI infrastructure, the number that decides the bill is what share of the day your hardware is actually working — which is a scheduling problem, not a purchasing one.

Source: [Hugging Face ↗](https://huggingface.co/blog/Dharma-AI/gpu-management)

---
**Fun fact:** Taxi drivers rarely die of Alzheimer's — years of building mental maps may protect the brain.

*Daily tech digest for curious professionals. AI news that affects your work.*