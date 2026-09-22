# Daily Tech Digest — Tuesday, September 22 2026

> A family's public plea about AI videos of a dead performer is the clearest test yet of who controls a person's face and voice.

---
## Robin Williams' daughter to fans making AI videos of him: 'Have some shame'

**What happened**
Zelda Williams asked fans publicly to stop making and sharing AI-generated videos of her late father, Robin Williams, telling them to "have some shame."

**What this means**
Generative video has made a recognisable face and voice cheap to reuse, and consent is now being argued in public rather than settled in court. If you work in marketing, comms or design, the safe assumption is that a real person's likeness is licensed material, not raw input.

Source: [Variety ↗](https://variety.com/2026/film/news/robin-williams-daughter-ai-videos-1236871568/)

---
## Quick Hits

### xAI released Grok 4.7

xAI published release notes for Grok 4.7, the latest update to the model behind its chatbot. Point releases land quietly but change day-to-day behaviour, so if Grok is part of your workflow it is worth re-testing the prompts you rely on.

Source: [xAI ↗](https://x.ai/news/grok-4-7)

### NASA's plan to bring Mars rocks home is dead

Science reports that Mars Sample Return, the long-planned effort to fly Martian rock samples back to Earth, has been cancelled. It closes out more than a decade of planning, and it is a reminder that the biggest science projects usually end on budget grounds rather than technical ones.

Source: [Science ↗](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead)

### Apple documents how to switch Apple Intelligence off

Apple published a support guide for turning off and restricting Apple Intelligence features on a Mac. If you handle confidential material — client files, student records, patient notes — this is the page to follow, or to forward to whoever manages your machines.

Source: [Apple Support ↗](https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac)

### The maths-and-AI question gets a formal advisory group

Previously covered on 2026-09-21: the mathematician Terence Tao wrote about what human mathematicians are still for now that machines can handle more of the proving. Since then, he has written about an Advisory Group on Mathematics and Artificial Intelligence — the same question, now handed to an organised body instead of argued in essays.

Source: [What's new (Terence Tao) ↗](https://terrytao.wordpress.com/2026/09/21/advisory-group-on-mathematics-and-artificial-intelligence/)

---
## Under the Hood

### tokenizers v1: the unglamorous step before the model, measured

**What happened**
Hugging Face released version 1.0 of tokenizers, the library that turns text into the numbers a model actually reads. The encode path was rebuilt around bitstreams instead of a regex split, with a word cache and a reworked merge loop, and the write-up publishes measured throughput rather than claims.

**Why it matters**
Tokenisation has never been the bottleneck in training, which is why it rarely got attention. It does sit on the path of every single request at inference time, so shaving it matters most to anyone serving a model at volume — and to anyone pushing large text corpora through a data pipeline.

```python
from tokenizers import Tokenizer

tok = Tokenizer.from_pretrained("bert-base-uncased")
enc = tok.encode("Tokenizers turn text into numbers.")
print(enc.ids)
print(tok.decode(enc.ids))
```

Source: [Hugging Face ↗](https://huggingface.co/blog/tokenizers-v1)

### Cutting layers out of a model, framed as a physics problem

**What happened**
Multiverse Computing treats the choice of which transformer blocks to delete as an energy-minimisation problem — an Ising model, the same maths used to describe magnets — rather than scoring each block on its own. Blocks interact, so dropping the two that individually look least useful is not the same as dropping the best pair. They solve it exactly where that is possible and with quantum-inspired methods where it is not, and report the approach holds up beyond dense transformers.

**Why it matters**
Pruning is how a large model gets small enough to run on hardware you actually own. Picking blocks jointly instead of ranking them one by one is the kind of change that decides whether the compressed version keeps the original's quality or quietly loses it.

Source: [Hugging Face ↗](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an)

---
**Fun fact:** Socrates argued writing would ruin memory. Today's "AI will rot your brain" worry is 2,400 years old.

*Daily tech digest for curious professionals. AI news that affects your work.*