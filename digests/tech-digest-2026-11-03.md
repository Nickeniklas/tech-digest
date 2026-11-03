# Daily Tech Digest — Tuesday, November 3 2026

> If you work for yourself, the US government's cybersecurity agency has just written a security guide with you in mind.

---
## NIST publishes a cybersecurity guide for the self-employed

**What happened**
NIST, the US agency that sets widely used cybersecurity standards, has released a cybersecurity guide written specifically for self-employed people and solopreneurs. Most security advice assumes you have an IT department; this one is aimed at people who don't.

**What this means**
If you freelance or run a one-person business — as a designer, consultant, lawyer, tutor or marketer — you are your own IT team, and your client files and accounts are just as attractive to attackers. A guide pitched at your situation is a practical place to start checking your basics.

Source: [NIST ↗](https://www.nist.gov/news-events/news/2026/11/self-employed-solopreneur-nist-has-cybersecurity-guide-just-you)

---
## Quick Hits

### Ubuntu still hasn't patched a critical Linux flaw after nearly three weeks

Previously covered on 2026-11-01: a Linux networking bug, CVE-2026-98432, rated 9.8 out of 10 for severity. Since then, a report says Ubuntu's long-term-support versions still have no fix almost three weeks on. If your organisation runs Ubuntu servers, it's worth asking your IT provider how they're handling it.

Source: [freenode.net ↗](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432)

### Terence Tao on 'egoless mathematics' in the AI era

Previously covered on 2026-11-02: Tao's essay arguing that mathematics has changed. Since then, the Fields Medal-winning mathematician has followed up with a new essay, 'Egoless Mathematics in the AI Era', continuing his look at how AI is reshaping the way research gets done and credited.

Source: [Terence Tao ↗](https://terrytao.wordpress.com/2026/11/02/egoless-mathematics-in-the-ai-era/)

### An essay on resisting 'cognitive surrender' to AI

A widely discussed essay, 'Resisting Cognitive Surrender', looks at the risk of handing over your thinking — not just your tasks — to AI tools. If you use AI daily at work, it's a useful prompt to notice which judgements you still make yourself.

Source: [knlb.dev ↗](https://knlb.dev/essays/surrender)

### If you love a website, back it up

A popular blog post makes a simple case: websites you rely on can vanish, so save copies of the ones that matter to you. Worth a thought if your work depends on reference pages, guides or tools hosted by someone else.

Source: [Misty's Internet ↗](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/)

---
## Under the Hood

### Cloudflare halves DNS build delay and cuts memory use by 85%

**What happened**
Cloudflare describes switching to targeted zone builds in its DNS system — the internet's address book, which turns website names into server addresses. Instead of rebuilding large amounts of data when something changes, it rebuilds only the affected zones, halving the delay before changes take effect and cutting memory use by 85%.

**Why it matters**
When you update a DNS record, how quickly that change spreads matters for launches and outages. It's also a clean example of a common engineering win: doing less work by rebuilding only what changed.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/dns-targeted-zone-builds/)

### OpenAI explains how it scales Git

**What happened**
OpenAI published an engineering post on scaling Git — the tool developers use to track every change to their code — inside the company. It lands the same week GitHub described moving its repositories to new infrastructure for 'agent-scale' workloads.

**Why it matters**
AI coding agents make far more code changes than people do, and the plumbing that stores and syncs code is being rebuilt to keep up. For engineering teams, these posts are a preview of the load their own tools will face.

Source: [OpenAI ↗](https://openai.com/index/scaling-git-at-openai/)

---
**Fun fact:** GitHub says it has already copied 99.99999% of its repositories to Azure — the last 0.00001% is the hard part.

*Daily tech digest for curious professionals. AI news that affects your work.*