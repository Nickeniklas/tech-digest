# Daily Tech Digest — Tuesday, July 21 2026

> A hacker erased an entire country's record of who owns what — a stark reminder that our most important data is only as safe as its backups.

---
## A Hacker Erased Romania's National Land Registry

**What happened**
An attacker broke into Romania's national land registry and wiped its database — the official record of who owns which piece of property across the country. Authorities are working to rebuild it from backups.

**What this means**
Land registries are the paper trail behind every home sale, mortgage, and boundary dispute. When one goes dark, property deals can freeze and ownership becomes hard to prove — a reminder for anyone in law, real estate, or finance that even the dullest official records now live or die by how well they're backed up and defended.

Source: [Risky Business ↗](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/)

---
## Quick Hits

### NVIDIA Builds an AI That Learns How the Physical World Moves

NVIDIA released Cosmos 3 Edge, a model that predicts how a scene will change so robots, warehouse machines, and self-driving systems can anticipate what happens next instead of only reacting. It's designed to run on the device itself rather than in the cloud, which matters for anything that has to respond in real time.

Source: [Hugging Face ↗](https://huggingface.co/blog/nvidia/cosmos3edge)

### A Small, Specialised Model Still Beats the Big New Ones

Dharma AI showed that its compact text-recognition model, tuned specifically for Brazilian Portuguese, still reads scanned documents in that language more accurately than newer general-purpose systems. It's a practical argument that a focused tool can outperform a bigger, do-everything one.

Source: [Hugging Face ↗](https://huggingface.co/blog/Dharma-AI/newer-models-same-advantages)

### Surveillance-Camera Maker Accused of Misleading Officials

The ACLU published findings that Flock Safety, which sells automated license-plate-reading cameras to towns and police departments, repeatedly gave city councils and the public inaccurate claims about how its cameras are used. Communities weighing these systems now have reason to check the sales pitch against the record.

Source: [ACLU ↗](https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/flock-safety-credibility-lost-as-it-repeatedly-lies-to-city-councils-police-departments-and-public-across-the-country)

### Kimi Launches an AI Assistant Aimed at Office Work

Moonshot, the Chinese lab behind the Kimi chatbot, launched Kimi Work — a version pointed at everyday office tasks like handling documents and carrying out multi-step assignments. It's part of a wider shift from chatbots that answer questions toward assistants that actually do the work.

Source: [Kimi ↗](https://www.kimi.com/products/kimi-work)

---
## Under the Hood

### Squeezing 85 Billion Calculations a Second Out of One CPU Core

**What happened**
A developer hand-optimised the most basic operation in AI — multiplying two grids of numbers, known as a matrix multiply — to run at about 85 billion calculations per second on a single core of an AMD processor, with no graphics card involved. Most of the speed comes not from a faster chip but from arranging the data so the processor's small, fast cache is reused instead of constantly fetching from slower main memory.

**Why it matters**
Matrix multiplication is the workhorse underneath every neural network. Seeing that careful memory layout — not raw clock speed — is what unlocks performance is the core lesson behind every fast AI library, from the ones on your laptop to the ones running in data centres.

```python
# Naive: jumps around memory, cache misses everywhere
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]

# Blocked: work on small tiles that fit in fast cache
for ii in range(0, N, TILE):
    for jj in range(0, N, TILE):
        for kk in range(0, N, TILE):
            multiply_tile(C, A, B, ii, jj, kk, TILE)
```

Source: [GitHub ↗](https://github.com/houslast3/85.30-GFLOPS-Single-Core-FP32-Matrix-Multiplication-on-AMD-Zen-3)

---
**Fun fact:** A hobbyist rebuilt San Francisco's Grace Cathedral as a 3D scene you can walk through in your browser.

*Daily tech digest for curious professionals. AI news that affects your work.*