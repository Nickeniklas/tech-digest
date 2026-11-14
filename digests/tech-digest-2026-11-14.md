# Daily Tech Digest — Saturday, November 14 2026

> The free software that lets you run AI models on your own laptop, instead of in someone else's cloud, has reached version 1.0.

---
## llama.cpp, the engine behind much of 'local AI', hits version 1.0

**What happened**
llama.cpp — open-source software that runs AI models directly on your own computer rather than on a company's servers — has released version 1.0.0, alongside a 1.0 of ggml, the library it is built on. Its makers say it runs models that handle text and images on everything from ordinary laptops to large business servers.

**What this means**
Many 'private' or offline AI apps quietly rely on llama.cpp, so a stable 1.0 makes that whole ecosystem more dependable. If you handle sensitive material — lawyers with client files, teachers with student records, HR with personnel data — keeping AI on your own machine is getting more practical.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

---
## Quick Hits

### US flights halted nationwide for 4.5 hours

The FAA ordered a nationwide ground stop on departing flights, lifting it about 4.5 hours later, NBC News reports. Amtrak's booking system also ran into major problems as travelers looked for alternatives. If you had travel planned, expect knock-on delays and rebookings.

Source: [NBC News ↗](https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247)

### XYBench tests whether AI can help when you ask the wrong question

The Allen Institute for AI released XYBench, a set of more than 8,000 questions built on misconceptions, to test whether assistants spot the real problem behind a request. Useful help often means gently pointing out that you're asking the wrong thing — this measures exactly that.

Source: [Hugging Face Blog ↗](https://huggingface.co/blog/allenai/xybench)

### Security agencies found using an ad-based surveillance system

Researchers at Citizen Lab report that security agencies in several countries use a surveillance system built on online advertising data. It's a reminder that the data collected to target ads can also be used to track people.

Source: [Citizen Lab ↗](https://citizenlab.ca/security-agencies-worldwide-found-to-use-ad-based-surveillance-system/)

### Accessibility statements get a home on GitHub

GitHub now highlights ACCESSIBILITY.md files, where project maintainers can document accessibility goals, known barriers and how to report problems. If you depend on assistive technology, it becomes easier to see up front whether a tool will work for you.

Source: [GitHub Blog ↗](https://github.blog/open-source/maintainers/accessibility-statements-now-have-a-home-on-github/)

---
## Under the Hood

### GitHub's October outages: eight incidents, up from two

**What happened**
GitHub's monthly availability report says it had eight incidents in October 2026 that degraded performance across its services, compared with two in September. The reports break down what went wrong and what GitHub changed afterward.

**Why it matters**
GitHub is where most software teams store and ship code, and it is in the middle of moving its storage onto new infrastructure built for AI agents. Teams that rely on it for deployments should treat these reports as a signal for how much redundancy to build in.

Source: [GitHub Blog ↗](https://github.blog/news-insights/company-news/github-availability-report-october-2026/)

---
**Fun fact:** GitHub logged eight service incidents in October 2026 — four times September's two.

*Daily tech digest for curious professionals. AI news that affects your work.*