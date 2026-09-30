# Daily Tech Digest — Wednesday, September 30 2026

> A week after GPT-6 launched, OpenAI has already shipped an update it says gets close to its top model at a fifth of the price.

---
## GPT-6.1 Sol: near-top performance at a fifth of the price

**What happened**
Previously covered on 2026-09-23: OpenAI released GPT-6 in two versions, Sol and Luna. Since then, OpenAI has released GPT-6.1 Sol, which it describes as offering intelligence close to its Astra model for a fifth of the price.

**What this means**
If the claim holds, the capable AI behind the tools you already use gets cheaper to run, which tends to show up as higher usage limits or lower prices. It's also a reminder that the model you chose last month may already have a cheaper successor.

Source: [OpenAI ↗](https://openai.com/index/introducing-gpt-6-1-sol/)

---
## Quick Hits

### OpenAI introduces Dots, agents that stay on

OpenAI announced Dots, which it describes as always-on agents. Instead of waiting for you to type a request, the idea is an assistant that keeps running in the background. Worth watching if you want AI to handle ongoing tasks rather than one-off questions.

Source: [OpenAI ↗](https://openai.com/index/introducing-dots/)

### NVIDIA releases a free model that predicts spreadsheet columns without training

NVIDIA published Kumo Tabular, an open model for table-shaped data. Give it a table with some rows already labelled, and it predicts labels for new rows in one step — no training, tuning or data preparation. For anyone forecasting from spreadsheets, this lowers the bar for getting a usable prediction.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/nvidia/kumo-tabular)

### How Delhi cut electricity losses from 50% to 5%

IEEE Spectrum looks at how Delhi reduced the share of electricity lost between the power plant and the customer from about half to about one in twenty. Lost power includes theft and billing gaps, not just worn wires. It's a case study in fixing infrastructure with better measurement.

Source: [IEEE Spectrum ↗](https://spectrum.ieee.org/delhi-electricity-loss)

### Vermont is swapping power plants for home batteries

The BBC reports on a "virtual power plant" in Vermont: batteries in ordinary homes, pooled together, that keep the lights on during storms. The approach replaces some traditional power plants with equipment people already have in their garages.

Source: [BBC Future ↗](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms)

---
## Under the Hood

### Checking that an AI agent cited the right source, not just a true fact

**What happened**
Multiverse Computing published ProvenanceGuard, a checker for AI agents that pull information from several tools at once. It tests whether each claim is backed by the specific source the agent credits, rather than by something found somewhere, and can repair answers it blocks.

**Why it matters**
When an agent reads from many similar-looking sources, a correct fact attributed to the wrong document is still a citation error. For research, legal and reporting work, where you need to know where a claim came from, that distinction matters.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source)

### Cloudflare is building a certificate authority for the whole internet

**What happened**
Cloudflare wrote about building its own certificate authority — the kind of organisation that issues the certificates behind the padlock icon in your browser, which prove a website is who it claims to be.

**Why it matters**
Only a small number of certificate authorities secure most of the web, so a new large-scale one changes who holds a key piece of internet trust. It's aimed at site operators and infrastructure teams.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/cloudflare-certificate-authority/)

---
**Fun fact:** Someone built a working computer from 277,248 identical NAND logic gates.

*Daily tech digest for curious professionals. AI news that affects your work.*