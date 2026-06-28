# Daily Tech Digest — Sunday, June 28 2026

> Ford bet big on replacing workers with AI — and is now learning, in public, what the technology still can't do.

---
## Ford Swapped Workers for AI. It Backfired.

**What happened**
Ford moved to automate parts of its operations with AI and cut human staff to do it, but the rollout went badly enough that the company is now dealing with the fallout rather than the savings it expected.

**What this means**
It's a useful reality check for anyone under pressure to replace people with AI quickly. The lesson isn't that AI doesn't work — it's that handing over a job humans were quietly holding together often exposes how much judgment that job actually required. Managers weighing automation should pilot narrowly before cutting headcount.

Source: [The Independent ↗](https://www.the-independent.com/tech/ford-ai-automation-human-workers-b3003787.html)

---
## Quick Hits

### An AI That Builds Real, Editable Slide Decks

A new open-source tool called PPT Master turns any document into an actual PowerPoint file — native shapes, animations, and speaker notes you can edit, not just a flat image of a slide. It can even narrate the notes as audio or follow your own template. If you make decks for a living, this is the kind of tool worth watching.

Source: [GitHub ↗](https://github.com/hugohe3/ppt-master)

### Asia Builds Its Own Answer to a Blocked AI Model

After the U.S. restricted who can use Anthropic's powerful Mythos model, several Asian AI startups have begun shipping their own Mythos-like systems. It's an early sign that export controls on top-tier AI may push other countries to build alternatives rather than wait for access. For businesses, it likely means more capable AI options outside the handful of U.S. providers.

Source: [TechCrunch ↗](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)

### GitHub and the UN Bring Open Source to Ghana

GitHub teamed up with the United Nations Development Programme in Ghana to explore how openly shared, freely reusable software can support the country's digital reform plans. The idea is that public-sector projects can build on shared code rather than paying for closed systems from scratch. It's a small but concrete example of open source reaching beyond the tech industry.

Source: [GitHub Blog ↗](https://github.blog/open-source/social-impact/github-and-undp-team-up-to-advance-development-priorities-in-ghana-with-open-source/)

---
## Under the Hood

### How 'Speculative Decoding' Makes AI Answer Faster

**What happened**
DeepSeek published work on DSpark, an implementation of a technique called speculative decoding. Normally a large language model writes one word at a time, and each word means another slow trip through a huge model. Speculative decoding adds a small, fast 'draft' model that guesses several words ahead; the big model then checks the whole guess in a single pass, keeping the parts it agrees with.

**Why it matters**
This is one of the main reasons today's chatbots feel snappy despite running enormous models — you get more words per expensive computation. It matters most to anyone running AI at scale, where speed and compute cost are the same problem.

```python
# Speculative decoding, in essence
draft = small_model.guess(prompt, n=4)    # cheap guess of the next 4 words
checked = big_model.verify(prompt, draft) # one pass confirms or corrects them
output += checked.accepted                # keep what the big model agreed with
# repeat from the last accepted word
```

Source: [DeepSeek ↗](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

### AI Takes On the 'Dark Art' of Radio Chip Design

**What happened**
Designing the analog radio circuits inside phones and Wi-Fi gear is notoriously hard — it leans on intuition and experience that engineers half-jokingly call a dark art. Researchers showed an AI system that can lay out parts of these radio-frequency chips, navigating trade-offs that usually take a human specialist days of fiddling.

**Why it matters**
Most AI-for-chips work has focused on digital logic; the messy analog world has resisted automation. If AI can reliably handle even slices of it, chip design gets faster and less dependent on a small pool of rare experts — which eventually shows up as cheaper, better wireless devices.

Source: [IEEE Spectrum ↗](https://spectrum.ieee.org/ai-radio-chip-design)

---
**Fun fact:** A new tool builds a real, editable PowerPoint from any document — shapes, speaker notes, and narration included.

*Daily tech digest for curious professionals. AI news that affects your work.*