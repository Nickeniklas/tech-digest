# Daily Tech Digest — Wednesday, November 25 2026

> A new paper claims a big leap on one of computing's oldest math problems — how fast a computer can multiply large grids of numbers.

---
## A paper claims matrix multiplication can be done far faster than anyone had shown

**What happened**
A preprint posted in OpenAI's public math repository claims that multiplying two large grids of numbers (matrices) can be done in roughly n^2.25 steps — a much bigger improvement than the tiny gains this problem has seen in decades. It is a claim for now: other mathematicians still need to check the proof.

**What this means**
Matrix multiplication is the core arithmetic behind AI models, graphics and scientific simulation, so this is mostly a landmark for theory rather than something that speeds up your apps tomorrow. Watch for whether experts confirm it — and how much AI helped produce it.

Source: [OpenAI math preprints (GitHub) ↗](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

---
## Quick Hits

### OpenAI says GPT-6 models can design proteins without special training

OpenAI reports that its GPT-6 models show built-in ability to design proteins, the molecules that do most of the work inside living cells. Until now, this has largely been the job of specialised biology AI tools. If it holds up, general-purpose chatbots could become useful lab assistants for drug and materials research.

Source: [OpenAI ↗](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)

### Anthropic maps out scenarios for how AI could reshape the economy

Anthropic published a set of possible economic futures — from rapid growth to widespread job loss, or neither — and the signs that would tell you which one is unfolding. It's a useful frame if you're planning a career, a team, or a budget around AI without knowing where it's heading.

Source: [Anthropic ↗](https://www.anthropic.com/institute/econ-scenarios)

### Sandboxed AI models can still pass messages to each other

A new write-up shows that AI models locked inside separate sandboxes can still communicate through the shared servers that run them. That matters for any organisation relying on isolation to keep AI agents — and the data they handle — apart.

Source: [LessWrong ↗](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being)

### Hackers are actively targeting Check Point security servers

Security firm GreyNoise reports an active intrusion campaign against Check Point's management servers, which many companies use to control their firewalls. If your organisation uses Check Point, it's worth making sure your IT team has seen this.

Source: [GreyNoise ↗](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)

---
## Under the Hood

### Running an AI model across 5,600 cloud functions — at 80x negative profit

**What happened**
A developer split the open Qwen model across about 5,600 AWS Lambda functions — small, pay-per-second cloud programs — to serve it without renting a GPU. It worked, and by their own account cost about 80 times more than it could earn.

**Why it matters**
It's a fun, concrete lesson in why AI runs on dedicated GPUs: chopping a model into thousands of tiny serverless pieces drowns it in network traffic and per-call costs. Useful reading for anyone estimating what it really costs to host a model.

Source: [noahbuilt.it ↗](https://noahbuilt.it/writing/qwen-on-5600-lambdas)

### Teaching a small walking robot to dodge obstacles in simulation first

**What happened**
NVIDIA published a tutorial on adding obstacle avoidance to Microduck, a small walking robot, without retraining how it walks. The robot is trained in a simulated world (Isaac Lab, with simulated distance sensors) and then the controller is moved onto the real hardware — a workflow called sim-to-real.

**Why it matters**
Training in simulation is how most modern robots learn safely and cheaply. Keeping the walking skill fixed and layering a separate steering controller on top is a practical pattern for robotics hobbyists and teams alike.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance)

---
**Fun fact:** Researchers built a rewritable display that keeps showing its image for months with no power at all.

*Daily tech digest for curious professionals. AI news that affects your work.*