# Daily Tech Digest — Tuesday, November 10 2026

> Anthropic has upgraded its two most capable AI models, and an independent ranking already puts one of them at the top.

---
## Anthropic releases Claude Fable 5.2 and Claude Mythos 5.2

**What happened**
Anthropic has upgraded Claude Fable and Claude Mythos, the models it builds for its hardest technical work, saying the 5.2 versions set a new bar in coding, finance and the sciences. Independent tester Artificial Analysis gave Fable 5.2 a score of 65 on its index, the highest it has recorded so far.

**What this means**
If you use Claude for long reports, financial analysis or research-heavy work, these are the versions to try on your hardest tasks. One widely shared post describes Fable 5.2 building a working game from a child's description in a single attempt, which gives you a sense of how much it can do from a plain request.

Source: [Anthropic ↗](https://www.anthropic.com/claude-fable-and-mythos-5-2)

---
## Quick Hits

### Claim: Gemini sends some personal Drive files and emails to human reviewers

A GitHub repository that drew wide attention on Hacker News claims that Google Gemini routes personal Google Drive files and emails to human annotators, the people who review AI output to improve it. Google has not confirmed this in the source. If you connect Gemini to work documents or client email, check your Gemini activity and privacy settings before sharing anything sensitive.

Source: [GitHub ↗](https://github.com/thisisme6598/gemini_files/)

### Canada launches Real-Time Rail, a 24/7 instant payment system

Payments Canada has launched Real-Time Rail, a national system that lets money move between accounts instantly, any hour of any day. For freelancers and small businesses, that means payments that no longer wait for banking hours or the next business day.

Source: [Payments Canada ↗](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy)

### Meta introduces Muse Ember, its smallest and most efficient model

Meta has released Muse Ember, which it calls the smallest and most efficient model in its Muse family. Small models like this are cheaper to run and can work on phones and laptops, which is where many everyday AI features end up.

Source: [Meta AI ↗](https://research.meta.ai/blog/muse-ember)

### Parking apps charge a median $0.35 convenience fee per session

A new dataset from ParkGraph tracks the extra convenience fees parking apps add in 312 US cities, and finds a typical charge of 35 cents each time you park. It is a small amount per use, but it adds up if you park in the city every working day.

Source: [ParkGraph ↗](https://parkgraph.com/parking-app-fees)

---
## Under the Hood

### HOPE: shrinking 'mixture-of-experts' models by keeping expert partners together

**What happened**
Amazon researchers describe HOPE, a method for pruning mixture-of-experts (MoE) models. An MoE model is split into many small specialist sub-networks, called experts, and only a few are used for each word, but every expert still has to sit in memory. HOPE removes experts while accounting for which ones tend to work in pairs, so cutting one doesn't quietly break its partner.

**Why it matters**
Memory, not compute, is often what makes large MoE models expensive to host. Smarter pruning means the same model can run on fewer or cheaper machines, which matters for anyone self-hosting open models.

Source: [Hugging Face Blog (Amazon) ↗](https://huggingface.co/blog/amazon/higher-order-pruning-experts)

### E-means claims to beat k-means in a tenth of the training passes

**What happened**
A new clustering method called E-means says it outperforms k-means, the classic algorithm for grouping similar data points, while needing only one-tenth as many epochs, or full passes over the data.

**Why it matters**
k-means sits inside countless tools, from customer segmentation to image compression. A drop-in alternative that converges ten times faster would cut compute time on large datasets.

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.random.rand(1000, 2)
km = KMeans(n_clusters=3, n_init=10).fit(X)
print(km.n_iter_, km.inertia_)
```

Source: [E-means ↗](https://e-means.github.io/)

---
**Fun fact:** Google's newest AI chips have names that sound like phone models: TPU 8tx and TPU 8i Max.

*Daily tech digest for curious professionals. AI news that affects your work.*