# Daily Tech Digest — Friday, October 30 2026

> Mistral has made one of the largest AI models yet free to download, so companies can run a top-tier assistant on their own computers.

---
## Mistral releases Large 4 as a free, downloadable model

**What happened**
French AI company Mistral released the weights of Mistral Large 4 — the files you need to run the model yourself — and it is now on Hugging Face. It reads text and images, works in many languages, and can take in about 1 million tokens (roughly several long books) at once.

**What this means**
Organisations that can't send data to an outside AI service, such as law firms, hospitals or public agencies, get another high-end option they can run in-house. Running a model this size still takes serious hardware, so for most people it will arrive through the IT department or a provider rather than a laptop.

Source: [Hugging Face ↗](https://huggingface.co/blog/mistral-large4)

---
## Quick Hits

### Study: school-wide phone bans show no clear mental health effect

A study in JAMA Network Open found that school-wide phone bans had no significant impact on students' mental health. If you teach or set school policy, it's a useful data point: bans may still help with focus or classroom behaviour, but this research doesn't support them as a mental health fix.

Source: [JAMA Network Open ↗](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2855858)

### $5.6 billion reported stolen from Binance

Blockchain tracking site Arkham is tracking an entity it labels a Binance hacker, linked to about $5.6 billion stolen from the cryptocurrency exchange. If confirmed, it would rank among the largest crypto thefts on record — a reminder that money held on an exchange carries risks your bank account doesn't.

Source: [Arkham ↗](https://arkm.com/explorer/entity/21a94755-f604-45e5-9501-6542e23005e8)

### Project ProtoStar aims to make public research easier for AI to use

Hugging Face announced Project ProtoStar, which brings together universities, research organisations, industry and the open science community. The goal is to make publicly funded research easier to find, reuse and build on — including by AI tools that researchers, students and journalists already rely on.

Source: [Hugging Face ↗](https://huggingface.co/blog/announcing-project-protostar)

### New open models for speech and decisions on Apple devices

Hugging Face introduced AnySpeechRecognizer and AnyDecisionModel, open models built to run on Apple platforms. Models that run on your own iPhone or Mac can turn speech into text without sending your recordings to a server.

Source: [Hugging Face ↗](https://huggingface.co/blog/anydecisionmodel)

---
## Under the Hood

### Granite Switch 4.1.1: updating AI models like software

**What happened**
IBM released Granite Switch 4.1.1, a little over a week after Granite Switch 4.1. Its modular design lets you add specialised add-ons called adapters to one language model on a single endpoint, and this release shows those add-ons can be updated the way you'd ship a software update.

**Why it matters**
Teams can add or refresh a model's expertise in one area without retraining or redeploying the whole model. For companies running their own AI, that means smaller, cheaper, more frequent updates.

Source: [Hugging Face ↗](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1)

### Shrinking a small model's vocabulary cuts running costs by 77%

**What happened**
Dharma AI reports that specialising the vocabulary of small language models — trimming the set of word-pieces a model knows down to those a given application actually uses — cut inference cost, the cost of running the model, by up to 77% in real applications.

**Why it matters**
For narrow, high-volume tasks like classifying support tickets, a tailored small model can be far cheaper to run than a general one. That's a practical route to lower AI bills.

Source: [Hugging Face ↗](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization)

---
**Fun fact:** Mistral's own nickname for its new trillion-parameter model is 'Le Chonk'.

*Daily tech digest for curious professionals. AI news that affects your work.*