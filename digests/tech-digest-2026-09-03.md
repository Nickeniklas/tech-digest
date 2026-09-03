# Daily Tech Digest — Thursday, September 3 2026

> A court decided Google gets to keep its advertising business intact — and researchers found 215,128 web pages built for no reason other than to be quoted by AI search engines.

---
## Google Keeps Its Ad Business in One Piece

**What happened**
A US court has decided what Google must do about its advertising technology business, and stopped short of ordering a breakup. Google had been found to hold illegal monopoly power in the tools that place ads across the web; the remedy is behavioural rather than structural.

**What this means**
If you buy or sell advertising — in marketing, publishing, or any business that runs campaigns — the plumbing you use stays where it is for now, rather than being split between new owners. The court's conditions will shape pricing and choice in that market over the next few years, but nothing changes in your ad account this week.

Source: [The New York Times ↗](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html)

---
## Quick Hits

### Thousands of Web Pages Exist Only to Be Quoted by AI

A report found three websites that between them published 215,128 "best software" pages — pages written not for readers but to be picked up and cited by AI search engines, and Perplexity does cite them. If you ask an AI assistant which tool to buy, some of its confident recommendations trace back to content manufactured for exactly that purpose. Worth checking who is actually behind a recommendation before you act on it.

Source: [Trellner ↗](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/)

### Google Ships Gemini 3.8 Flash, Plus a Version Built for Security Work

Google released Gemini 3.8 Flash, the fast and cheap tier of its model family, alongside a variant aimed specifically at cybersecurity tasks. Flash models are the ones that tend to end up inside everyday products — chat assistants, document tools, customer support — because they are quick enough to feel instant.

Source: [Google ↗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

### Research Says the World's Writing Is Getting More Alike

A paper in Nature Human Behaviour reports that the range of language people use is narrowing as large language models spread — the same phrasings and structures turning up across more of what gets written. For anyone whose work is writing, that is an argument for keeping a recognisable voice rather than letting a model smooth it out.

Source: [Nature Human Behaviour ↗](https://www.nature.com/articles/s41562-026-02550-0)

### Why a Shorter AI Answer Can Cost You More

GitHub published what it learned about the cost of AI coding assistants, and the headline finding is counterintuitive: forcing a model to answer briefly often makes the whole job more expensive, because the short answer is wrong and the work gets redone. The same logic applies to any AI tool you pay for by usage — the cheap-looking setting is not always the cheap one.

Source: [The GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)

---
## Under the Hood

### BenchMIRT: What AI Benchmarks Are Actually Measuring

**What happened**
Allen Institute researchers borrowed a technique from educational testing — item response theory, the maths behind well-designed exams — and applied it to AI benchmarks. Instead of treating every question as worth the same, it works out which questions actually distinguish a strong model from a weak one. The result: most benchmarks carry a lot of dead weight, and a much smaller set of well-chosen questions measures the same thing.

**Why it matters**
Benchmark scores are how models get compared in press releases and procurement decisions, and they are noisier than the headline numbers suggest. Knowing which questions do the discriminating means cheaper evaluation runs and a clearer read on whether a new model is genuinely better or just better at the test.

Source: [Hugging Face / Allen Institute for AI ↗](https://huggingface.co/blog/allenai/benchmirt)

### Cloudflare Wants to Recompress the Cached Web

**What happened**
Cloudflare stores copies of web files close to users so pages load fast, and much of that cache is compressed with older formats. The company is looking at transcoding it — quietly recompressing stored files with Zstandard, a newer and more efficient compression format, handled inside Pingora, the proxy it wrote to replace Nginx. The saving it estimates runs to petabytes.

**Why it matters**
Nothing about the files changes from a visitor's point of view; the same bytes come out the other end. It is a reminder that at internet scale, swapping one compression algorithm for another is a storage decision measured in warehouses of disks, not percentages.

Source: [The Cloudflare Blog ↗](https://blog.cloudflare.com/cache-transcoding/)

---
**Fun fact:** Three websites published more "best software" pages than most encyclopedias have articles.

*Daily tech digest for curious professionals. AI news that affects your work.*