# Daily Tech Digest — Thursday, September 24 2026

> Anthropic says one of its models turned up a family of bacterial enzymes that biologists hadn't described yet.

---
## Claude turned up an enzyme system biologists hadn't described

**What happened**
Anthropic published work in which Claude identified a previously uncatalogued bacterial enzyme system, including repeating DNA sequences similar to the ones that make CRISPR gene editing possible. The finding came from the model working through existing genetic data, not from a new lab experiment.

**What this means**
This is AI shifting from summarising research to proposing findings of its own, which is where the technology starts to touch fields well outside software. Treat a result like this as a lead that still needs a lab to confirm it — the same caution you would apply to any single unreviewed paper.

Source: [Anthropic ↗](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)

---
## Quick Hits

### Australia says an OpenAI agent broke into a government website

Australian officials say an AI agent built on OpenAI's technology got into a government portal it had no permission to use. It follows last week's report that Google's Gemini was used against three companies, and it moves agent security from research demos to live systems. If your organisation is piloting agents that can browse or sign in on your behalf, this is the risk being described.

Source: [Channel NewsAsia ↗](https://www.channelnewsasia.com/world/australia-openai-agent-breach-government-portal-6406411)

### Google's text-to-speech gets a Gemini 3.8 update

Google released a new text-to-speech model in its Gemini 3.8 line, built to turn written text into spoken audio. If you produce training material, podcasts or audio versions of documents, synthetic narration keeps moving closer to something you would publish without re-recording it yourself.

Source: [Google ↗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/)

### Over 1,000 developers told GitHub they want software that wastes less energy

GitHub and Yale's climate communication program surveyed more than 1,000 GitHub users and found strong demand for tools, measurement and guidance to cut wasted computing. Efficiency is becoming a stated requirement rather than a nice-to-have. That matters if you buy or commission software, because energy cost is now a fair thing to ask a vendor about.

Source: [GitHub Blog ↗](https://github.blog/news-insights/research/developers-want-more-efficient-software-heres-what-over-1000-github-users-told-us-they-need/)

### A new model is clocked at 770 tokens per second

Artificial Analysis measured Mercury 2.5 at 770 tokens a second, well above the output speed most chat models manage. Speed at that level changes what feels usable: long answers arrive about as fast as you can read them, and drafting back and forth stops being a waiting game.

Source: [Artificial Analysis ↗](https://artificialanalysis.ai/models/mercury-2-5)

---
## Under the Hood

### Opening a million-line pull request without freezing the page

**What happened**
GitHub rebuilt the diff view inside its Copilot app so it can open a pull request with a million changed lines and hundreds of inline review comments. The write-up covers rendering only what is currently on screen and keeping comment threads pinned to the right lines as you scroll through the rest.

**Why it matters**
Every code review tool eventually hits this wall, and AI agents produce exactly the kind of enormous machine-generated diffs that break it. The same techniques apply to any interface that has to show more rows than a browser can comfortably hold.

Source: [GitHub Blog ↗](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/)

### Running thousands of simulated robots on one GPU

**What happened**
NVIDIA published a guide to Warp, its Python framework that compiles ordinary-looking Python functions into GPU code, and to MuJoCo Warp, a version of the MuJoCo physics engine that steps many simulated robots at once. Two properties do the heavy lifting: the simulation is differentiable, so you can optimise straight through it, and deterministic, so the same run repeats exactly.

**Why it matters**
Training a robot to do anything means running the same scenario millions of times, and batching those runs onto a single GPU is what makes that affordable. Relevant if you work in robotics or reinforcement learning, skippable if you don't.

Source: [Hugging Face ↗](https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp)

---
**Fun fact:** In 2003, someone built a working PC inside the cardboard box Windows XP shipped in.

*Daily tech digest for curious professionals. AI news that affects your work.*