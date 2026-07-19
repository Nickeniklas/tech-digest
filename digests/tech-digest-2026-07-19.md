# Daily Tech Digest — Sunday, July 19 2026

> An AI model just helped close a math problem that had stood open for three decades — and a quieter fight over AI-faked apartment photos is heading to court.

---
## An AI Model Helped Close a 30-Year-Old Math Problem

**What happened**
Days after OpenAI reported that its systems contributed to a research proof, mathematicians on Reddit documented how a single prompt to GPT-5.6 helped close a roughly 30-year-old open gap in convex optimization — a branch of math used to find the best solution when many constraints pull against each other.

**What this means**
AI is starting to do more than summarize known work; it is helping produce results that professional mathematicians had not cracked. For anyone whose field relies on optimization — logistics, finance, scheduling, engineering — it hints that these tools may soon suggest genuinely new methods, not just tidy up old ones.

Source: [r/math (Reddit) ↗](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/)

---
## Quick Hits

### New York Tells Landlords: No AI-Faked Apartment Photos

New York City's mayor said landlords can't quietly use AI-generated or heavily altered images to advertise rental units without disclosing it. The move targets listings that show apartments looking brighter, bigger, or better maintained than they really are. If you market property, sell homes, or write ad copy, expect disclosure rules around AI imagery to spread to more cities.

Source: [PetaPixel ↗](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)

### LG Monitors Quietly Installed Software Through Windows Update

Owners discovered that some LG monitors pushed their own software onto Windows PCs automatically, routed through the normal Windows Update process, without asking permission first. It is a reminder that even a screen can act as a channel for unwanted software. Anyone managing a fleet of office machines may want to check what their hardware is installing behind the scenes.

Source: [VideoCardz ↗](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent)

### One Chart Shows How AI Reshaped Stack Overflow

A single graph, drawn straight from Stack Overflow's own public data, shows how sharply activity on the long-running programming Q&A site has fallen since AI chatbots arrived — developers increasingly ask an assistant instead of posting a question. It is one of the clearest pictures yet of how AI tools are quietly hollowing out the community sites people used to rely on.

Source: [Stack Exchange Data Explorer ↗](https://data.stackexchange.com/stackoverflow/query/1953768#graph)

---
## Under the Hood

### The Cost of Saying Yes to New Code Has Changed

**What happened**
GitHub's engineering team argues that AI has made writing code cheap, but owning it — maintaining, securing, and understanding it over years — just as expensive as ever. They lay out a framework for deciding which new features and dependencies are actually worth taking on now that generating them is nearly free.

**Why it matters**
This reframes a debate playing out inside most software teams: if an AI can produce a feature in minutes, the real question becomes whether your team can afford to live with it for years. It is useful reading for anyone managing engineers or budgeting technical work.

Source: [The GitHub Blog ↗](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)

### Why Better Tools Made Copilot's Code Review Worse — Then Better

**What happened**
GitHub describes rebuilding how its Copilot code-review agent works. Giving the AI fancier, purpose-built tools actually made its reviews worse; performance improved only once the team switched it to simple, Unix-style commands for exploring code and grounded every comment in evidence from the pull request itself.

**Why it matters**
It is a concrete lesson for anyone building AI agents: more capable tools don't automatically mean better results, and forcing an agent to justify itself from real evidence beats handing it a bigger toolbox. Expect this 'less is more' pattern to show up across other AI assistants.

Source: [The GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/)

---
**Fun fact:** Speech recognition and text-to-speech now fit in under 500 kilobytes — smaller than a single phone photo.

*Daily tech digest for curious professionals. AI news that affects your work.*