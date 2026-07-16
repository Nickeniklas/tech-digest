# Daily Tech Digest — Thursday, July 16 2026

> The company started by OpenAI's former research chief just released its first open model that anyone can download and run for free.

---
## Thinking Machines Releases Its First Open Model, Inkling

**What happened**
Thinking Machines, the AI startup founded by OpenAI's former research lead Mira Murati, released Inkling — its first model with 'open weights,' meaning anyone can download it and run it on their own computers for free rather than renting access through a company's website.

**What this means**
Until now this well-funded lab had shipped nothing public, so a free, downloadable model is a real signal it intends to compete openly. For you, more capable open models mean the AI tools built into your work software get cheaper and can run privately, without your data leaving your organisation.

Source: [Thinking Machines ↗](https://thinkingmachines.ai/news/introducing-inkling/)

---
## Quick Hits

### xAI Opens Up the Code Behind Its Grok Coding Tool

Elon Musk's xAI published the full source code for Grok Build, its command-line assistant that helps developers write and edit software. Making the code public lets anyone inspect exactly how it works — useful timing, since a developer recently documented what an earlier version quietly sent back to the company.

Source: [xAI on GitHub ↗](https://github.com/xai-org/grok-build)

### A New Yardstick for How Human Voice Assistants Actually Sound

Hugging Face released Real World VoiceEQ, a test that measures how natural and human a voice AI feels to real people, not just whether it gets the words right. As talking assistants show up in phones, cars, and customer service lines, this gives buyers a way to compare them on the thing users actually notice — whether it sounds like a person or a robot.

Source: [Hugging Face ↗](https://huggingface.co/blog/real-world-voiceeq)

### A Full Firefox Web Browser Now Runs Inside a Web Page

Developers got the Firefox browser running entirely inside another browser tab, using a technology called WebAssembly that lets heavy desktop software run on a web page. It is mostly a technical showcase for now, but it hints at a future where full applications open instantly in a browser with nothing to install.

Source: [Puter Labs ↗](https://developer.puter.com/labs/firefox-wasm/)

---
## Under the Hood

### Running a Modern AI Model on a 13-Year-Old Server, No GPU

**What happened**
A tinkerer got Gemma 4 26B — a sizeable open model from Google — generating text at about 5 words per second on a 2013-era Xeon server with no graphics card, relying only on ordinary system memory and a lot of careful tuning.

**Why it matters**
Serious AI is usually assumed to need expensive graphics chips. Showing that older, cheap hardware can run a capable model — slowly but usably — matters for anyone running AI on a tight budget or where sending data to the cloud isn't an option.

```python
# Load a large model but keep it in ordinary RAM (CPU), not a GPU
from transformers import pipeline

gen = pipeline(
    "text-generation",
    model="google/gemma-4-26b",
    device_map="cpu",
)
print(gen("Explain photosynthesis simply:", max_new_tokens=60))
```

Source: [Neomind Labs ↗](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/)

### Why Automatically Routing Requests to Cheaper AI Models Is Harder Than It Looks

**What happened**
IBM researchers, writing on Hugging Face, walked through why a seemingly simple idea — send easy questions to a cheap AI model and hard ones to an expensive model — keeps tripping teams up. Cost, task difficulty, and speed all turn out to be messier to measure than they first appear.

**Why it matters**
'Model routing' is how many AI products quietly keep costs down behind the scenes. Understanding its pitfalls helps anyone building or buying AI tools judge whether a vendor's efficiency claims hold up in real use.

Source: [IBM Research on Hugging Face ↗](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt)

---
**Fun fact:** A hobbyist got a capable modern AI model running on a 13-year-old office server with no graphics card at all.

*Daily tech digest for curious professionals. AI news that affects your work.*