# Daily Tech Digest — Sunday, July 26 2026

> Cloudflare is handing website owners a switch to block or charge the AI bots scraping their pages.

---
## Cloudflare Lets Websites Block or Charge AI Crawlers

**What happened**
Cloudflare, which sits in front of a large share of the world's websites, rolled out new controls that let site owners decide how AI companies' bots may use their content — allow them, block them, or charge them per visit. It is turning on some of these protections by default for new customers.

**What this means**
If you publish anything online — a blog, a portfolio, a small business site — you have had little say in whether AI systems harvest it. This gives you a real off switch, and potentially a way to get paid. Marketers, writers, and designers who rely on web traffic are the most directly affected.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/content-independence-day-ai-options/)

---
## Quick Hits

### Thinking Machines Releases Its First Model, Inkling

Thinking Machines, the high-profile startup founded by former OpenAI leaders, published its first model, Inkling, on Hugging Face. It is the lab's opening move after months of building, and its release lets researchers and developers try the work directly rather than take the company's word for it.

Source: [Hugging Face ↗](https://huggingface.co/blog/thinkingmachines-inkling)

### Bitchat Resurfaces After India's Takedown Order

Previously covered on 2026-07-25: India ordered GitHub to remove Bitchat, Jack Dorsey's Bluetooth-based messaging app. Since then, the project has appeared on Radicle, a code-hosting network with no central company to send takedown notices to. It shows how hard it is to remove open-source software once it spreads.

Source: [Radicle ↗](https://radicle.network/nodes/rosa.radicle.network/rad%3Az2v9tRJz1oknFAqCSY5W5c76nVvm6)

### A Top Law School Rethinks How It Teaches for the AI Era

The University of Chicago Law School published a strategy for how legal education should change now that AI can draft, research, and review documents. If you work in law or hire lawyers, it is an early sign of which skills schools think will still matter — and which the software is expected to take over.

Source: [University of Chicago Law School ↗](https://www.law.uchicago.edu/news/ai-strategy-statement)

### GM Bets on Sodium Batteries for the Power Grid

General Motors is backing sodium-ion batteries — which swap out the scarce lithium found in most batteries for cheap, abundant salt — to store energy for the US electric grid. The trade-off is that they hold less energy for their size, which matters less for a stationary grid battery than for a car.

Source: [IEEE Spectrum ↗](https://spectrum.ieee.org/sodium-ion-battery-peak-energy)

---
## Under the Hood

### Running a 28.9M-Parameter Language Model on an $8 Chip

**What happened**
A developer got a small language model — 28.9 million parameters, tiny by modern standards — running on an ESP32, the roughly $8 microcontroller found in smart plugs and hobbyist gadgets. Big cloud models have hundreds of billions of parameters; this one is small enough to fit in a chip's few megabytes of memory and run with no internet connection.

**Why it matters**
It is a concrete look at how far models can be shrunk to run locally, on cheap hardware, with full privacy. That is the direction a lot of on-device AI — in appliances, toys, and sensors — is heading.

```python
# A parameter count is just weights x precision.
# 28.9M params at 8-bit = ~29 MB, too big for
# an ESP32's ~4 MB, so weights stream from flash:
params = 28_900_000
bytes_per_weight = 1        # 8-bit quantization
print(params * bytes_per_weight / 1e6, "MB")
# -> 28.9 MB stored, read in small chunks
```

Source: [GitHub ↗](https://github.com/slvDev/esp32-ai)

### Why Automatically Picking the Right AI Model Is Harder Than It Looks

**What happened**
IBM researchers dug into 'model routing' — the idea of automatically sending each question to the cheapest AI model that can still answer it well, and only escalating hard ones to an expensive model. In practice, reliably judging a question's difficulty before answering it turns out to be most of the problem.

**Why it matters**
Routing is how many companies plan to keep AI bills down as usage grows. This is a useful reality check for teams betting that a router will quietly cut their costs without hurting quality.

Source: [Hugging Face ↗](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt)

---
**Fun fact:** A working AI language model now fits on a microcontroller that costs about the same as a sandwich.

*Daily tech digest for curious professionals. AI news that affects your work.*