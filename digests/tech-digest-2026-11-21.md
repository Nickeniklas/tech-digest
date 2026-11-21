# Daily Tech Digest — Saturday, November 21 2026

> Mathematicians are scrambling to check a claimed proof of one of the most famous unsolved problems in math — and AI may have had a hand in it.

---
## A claimed proof of the Generalized Riemann Hypothesis has mathematicians buzzing

**What happened**
Mathematician Levent Alpöge has posted a claimed proof of the Generalized Riemann Hypothesis, a question about prime numbers that has stood unsolved for over a century, and leading mathematicians including Terence Tao are already writing about it. A widely shared post by computer scientist Scott Aaronson is titled "The stochastic parrots have apparently proved the Riemann Hypothesis", pointing to a role for AI language models.

**What this means**
Nothing is confirmed until experts finish checking the proof, which can take months. But if AI helped crack a problem this hard, it is a strong signal that these tools can contribute to original expert work, not just drafting and summarising — something researchers, analysts, and anyone in a knowledge profession should watch.

Source: [Hacker News / Scott Aaronson ↗](https://scottaaronson.blog/?p=10344)

---
## Quick Hits

### Inkling 2 Mini: a capable AI model built to run on your own computer

Thinking Machines released Inkling 2 Mini, an open model that can work with text and images and is designed for local use. It has about 26 billion parameters in total but uses only around 3 billion for each word, and reuses some of its layers in a loop to act like a bigger model. For you, that means more privacy and no subscription fees if you run AI on your own machine.

Source: [Hugging Face ↗](https://huggingface.co/blog/inkling2mini)

### Signal pushes back on AI agents reading your phone screen

Signal, the encrypted messaging app, published a post on restricting AI agents built into mobile operating systems from capturing your data. As phone makers add assistants that can see what is on your screen, it raises the question of whether private conversations stay private — relevant to anyone handling confidential client or patient information.

Source: [Signal ↗](https://signal.org/blog/protecting-your-privacy/)

### Backblaze's privacy policy now says it can sell data for advertising

Backblaze, a popular cloud backup service, now explicitly states in its privacy policy that it sells data for advertising purposes, according to a widely discussed Hacker News thread. If you or your organisation back up files there, it is worth reading the updated policy.

Source: [Backblaze ↗](https://www.backblaze.com/company/policy/privacy)

### Research paper: AI chatbots may carry hidden commercial incentives

A new paper calls it "The Hungry Butler Effect": concealed commercial incentives in large language models that can erode how rigorous their answers are. If you use AI to compare products or vendors, it is a reminder to check its recommendations against independent sources.

Source: [ResearchGate ↗](https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models)

---
## Under the Hood

### Valkey swaps the skiplist for a B+ tree and cuts memory use

**What happened**
Valkey, the open-source in-memory database that forked from Redis, replaced the skiplist behind its sorted sets with a B+ tree. Sorted sets power things like leaderboards and ranked feeds, and the change cuts their memory overhead by up to 43%.

**Why it matters**
In-memory databases are paid for by the gigabyte of RAM, so a structural change that trims overhead by this much translates directly into smaller servers and lower cloud bills for anyone running large ranked data sets.

Source: [Valkey ↗](https://valkey.io/blog/from-skiplist-to-b+tree/)

### Harness adapters: tuning a model for the agent tool you actually use

**What happened**
Hugging Face introduced harness adapters, a way to train an AI model with reinforcement learning on your own set of tasks inside your chosen agent harness — the software that wraps a model with tools and instructions.

**Why it matters**
Hugging Face reports that the adapted models become both more accurate and cheaper to run for that specific harness and workload, giving teams an alternative to simply paying for a bigger general-purpose model.

Source: [Hugging Face ↗](https://huggingface.co/blog/harness-adapters-at-scale)

---
**Fun fact:** Queen guitarist Sir Brian May, who holds a PhD in astrophysics, has contributed to ESA's Hera asteroid mission.

*Daily tech digest for curious professionals. AI news that affects your work.*