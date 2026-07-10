# Daily Tech Digest — Friday, July 10 2026

> The EU voted to have apps scan your private messages, OpenAI quietly shipped a new ChatGPT, and a hobby project now runs a capable AI on an ordinary laptop.

---
## The EU Votes to Scan Private Messages

**What happened**
The European Parliament approved a version of 'Chat Control,' a rule that would push messaging apps to scan the private chats and photos on your phone for illegal material before they are sent. Digital-rights advocates argue it weakens the encryption that keeps ordinary conversations private and would treat everyone as a suspect.

**What this means**
If this becomes law, the confidentiality you assume in apps like WhatsApp and Signal could erode across Europe. That matters most for anyone who handles sensitive information for a living — lawyers, doctors, journalists, and the people who confide in them — but it touches every private message you send.

Source: [Patrick Breyer ↗](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/)

---
## Quick Hits

### OpenAI Ships GPT-5.6

OpenAI released GPT-5.6, the newest version of the model that powers ChatGPT. The company published it with little fanfare, and a point-number update like this usually means quiet refinements rather than dramatic new abilities. Still, it is the tool millions of people reach for daily, so small changes ripple widely.

Source: [OpenAI ↗](https://openai.com/index/gpt-5-6/)

### An AI Tutor That Answers a Child in One Second

The team behind Ello, a reading app for young children, explained how they built an AI tutor that responds to a five-year-old in about a second — fast enough to feel like a real back-and-forth. For teachers and parents, it is a glimpse of what it takes to make AI feel patient and natural for kids learning to read.

Source: [Ello ↗](https://www.ello.com/blog/teaching-a-child-in-1000-ms)

### Running a Capable AI on an Ordinary Laptop

A developer shared Colibri, a project for getting GLM 5.2 — a powerful open AI model — running on a slow, everyday computer. It is another sign that useful AI is drifting away from expensive cloud servers and onto the hardware people already own, no monthly subscription required.

Source: [GitHub ↗](https://github.com/JustVugg/colibri)

---
## Under the Hood

### How GitHub Gave Every Repository a Durable Owner

**What happened**
GitHub found that of its 14,000-plus internal code repositories, fewer than half had a clear owner. Over 45 days it assigned every active repository a validated owner and archived the rest, then made ownership the foundation for security and maintenance decisions across the company.

**Why it matters**
'Who owns this code?' sounds trivial, but at scale it is the question that decides who fixes a bug, patches a vulnerability, or retires a dead project. This is a practical template for any large organization drowning in half-forgotten systems nobody is clearly responsible for.

Source: [GitHub Blog ↗](https://github.blog/security/application-security/how-github-gave-every-repository-a-durable-owner/)

### Making a Common AI Toolkit Run at Full Speed

**What happened**
Hugging Face rebuilt the link between its widely used 'transformers' library — the default way most open AI models are written — and vLLM, a system for serving those models quickly. Models defined in transformers can now run through vLLM as fast as hand-tuned custom code, with no extra work from the people who built them.

**Why it matters**
Running an open model fast in production used to require bespoke engineering for each one. Closing that gap means a new model can go from research code to fast, cheap serving almost immediately — which lowers the cost and delay of putting fresh AI into real products.

Source: [Hugging Face ↗](https://huggingface.co/blog/native-speed-vllm-transformers-backend)

---
**Fun fact:** For the first time in years, no leap second will be added to the world's clocks this December.

*Daily tech digest for curious professionals. AI news that affects your work.*