# Daily Tech Digest — Thursday, October 22 2026

> OpenAI's models are heading to Google Cloud, so the AI tools at your company may soon come from a cloud you already use.

---
## OpenAI's models are coming to Google Cloud

**What happened**
OpenAI announced that its AI models will be available through Google Cloud, one of the big three cloud platforms many businesses already pay for.

**What this means**
If your organisation runs on Google Cloud, you may soon be able to use OpenAI's models without signing a separate contract or moving data elsewhere. For managers and IT buyers, it means one less reason AI choice is tied to one vendor.

Source: [OpenAI ↗](https://openai.com/index/openai-models-google-cloud/)

---
## Quick Hits

### Australian court orders Apple to open up the iPhone

In the Epic vs. Apple case, Australia's Federal Court has ordered Apple to allow alternative app stores, sideloading (installing apps from outside the App Store) and third-party payments. If it stands, Australian iPhone users could get more ways to buy apps, and businesses selling through apps could avoid Apple's payment system.

Source: [Federal Court of Australia ↗](https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552)

### Meta ordered to pay $25 billion in New Mexico Cambridge Analytica case

CNBC reports that Meta has been ordered to pay a $25 billion penalty in New Mexico over the Cambridge Analytica scandal, in which Facebook users' data was harvested for political targeting. It's a large signal that privacy failures from years ago can still carry real costs.

Source: [CNBC ↗](https://www.cnbc.com/2026/10/21/meta-new-mexico-cambridge-analytica-penalty.html)

### A popular AI software tool was hijacked to steal passwords

Security firm SafeDep found that version 1.107.0 of LiteLLM — a widely used tool that connects apps to many AI models — was published with hidden code that steals login credentials and opens a backdoor. If your company's developers use it, ask them to check which version they installed.

Source: [SafeDep ↗](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)

### IBM releases Granite Speech 5.0

IBM published Granite Speech 5.0, a speech model it says transcribes, translates and identifies who said what more accurately and faster. That kind of tool is what powers meeting notes, interview transcripts and subtitles.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/ibm-granite/granite-speech-5)

---
## Under the Hood

### NVIDIA Kumo Relational predicts from business databases with no training

**What happened**
NVIDIA introduced Kumo Relational, a pre-trained model that makes predictions directly on company databases. Given a question, it gathers up to 10,000 historical examples as context and predicts outcomes like customer churn, demand or fraud in one pass — no model training required.

**Why it matters**
Building a custom prediction model usually takes a data science team weeks. A ready-made model that reads your existing tables could put forecasting within reach of smaller teams, and NVIDIA says it beats traditionally trained models on this kind of data.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/nvidia/kumo-relational)

### Trimming a small model's vocabulary cuts running costs by 77%

**What happened**
Dharma AI describes VocabX, a method for specialising the vocabulary of small language models. Models fine-tuned from general ones like Qwen and Gemma inherit a vocabulary built for every domain; shrinking it to fit the actual task cut inference cost — the cost of running the model — by 77% in real applications.

**Why it matters**
Much of what companies spend on AI is running models, not building them. A specialised model that does the same job for under a quarter of the cost makes narrow, in-house AI tools far cheaper to operate.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization)

---
**Fun fact:** A tiny possum and a glider thought extinct for 6,000 years have turned up alive in remote West Papua.

*Daily tech digest for curious professionals. AI news that affects your work.*