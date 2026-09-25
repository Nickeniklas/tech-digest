# Daily Tech Digest — Friday, September 25 2026

> A tutoring company is telling parents to keep their money and let AI do the tutoring instead — and that's the kind of shift worth watching wherever your job involves teaching or advising.

---
## A tutoring company tells parents: save your money, use AI instead

**What happened**
The Australian Financial Review reports that a tutoring company is advising parents to skip paid tutoring and have their children use AI tools instead. That's unusual advice, since it undercuts the company's own product.

**What this means**
When a business in the field says its own paid service can be replaced, it's worth noticing. Teachers should expect more students arriving with AI-assisted homework help, and anyone who sells expert advice by the hour — consultants, coaches, lawyers — may face the same question from clients.

Source: [Australian Financial Review ↗](https://www.afr.com/policy/health-and-education/tutoring-company-tell-parents-to-save-their-money-and-use-ai-instead-20260923-p60z0r)

---
## Quick Hits

### The UK's AI safety institute is opening up how it tests models

The UK AI Security Institute is publishing its evaluation results through the EvalEval Coalition's shared infrastructure, so others can check and repeat them. When you read that a model is safe or scores well, this makes it easier for someone independent to verify the claim.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/evaleval-aisi)

### Historians are using AI to decode 17th-century letters

A historian describes using language models to trace alchemical knowledge and read hard-to-decipher 17th-century correspondence, and argues AI labs should fund this kind of historical work. If you work with old archives, handwritten records or dense documents, it's a practical example of AI as a reading assistant.

Source: [Res Obscura ↗](https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical)

### Google's Project Suncatcher aims to put AI computing in space

Google published a fact sheet on Project Suncatcher, its research effort to run machine-learning infrastructure in orbit. The idea reflects how much power and space AI now demands on the ground.

Source: [Google Blog ↗](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/)

### GitHub: sometimes a chat box is the wrong way to work with AI

GitHub makes the case for "canvases" — shared workspaces you can see and edit — instead of typing everything into a chat window. If you've found yourself scrolling up through a long AI conversation to find the latest version of a document, this is the problem they're addressing.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/when-chat-is-the-wrong-ui/)

---
## Under the Hood

### Speeding up a vision model by letting a small model guess ahead

**What happened**
Liquid AI released an experimental DSpark draft model for its 3-billion-parameter vision-language model, LFM2.5-VL-3B. It uses speculative decoding: a small, fast model drafts the next few words and the larger model checks them in one pass, which cuts waiting time on both CPU and GPU. The write-up also covers where this trick works less well for image-heavy tasks.

**Why it matters**
Models that read images and text are usually slow on ordinary hardware. Speculative decoding is one of the few speed-ups that doesn't change the output, so it matters for anyone running these models on laptops or small servers.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark)

### GitHub's security team hands fuzzing to an AI agent

**What happened**
The GitHub Security Lab published a new fuzzing taskflow for its Taskflow Agent framework. Fuzzing means feeding software huge amounts of random or malformed input to find crashes; the agent handles much of the setup that usually makes this tedious.

**Why it matters**
Writing fuzzing harnesses is skilled, slow work, which is why many projects never do it. If an agent can take on the setup, more open-source code gets tested for the kinds of bugs attackers exploit.

Source: [GitHub Blog ↗](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/)

---
**Fun fact:** Aalto University hosts a Nokia Design Archive — decades of phone sketches, open for anyone to browse.

*Daily tech digest for curious professionals. AI news that affects your work.*