# Daily Tech Digest — Friday, July 24 2026

> The U.S. military flew a fighter jet with AI at the controls, a fight is brewing in Washington over Chinese open AI models, and warnings grow about hidden debt behind the AI boom.

---
## DARPA and the Air Force Fly an AI-Controlled F-16

**What happened**
DARPA and the U.S. Air Force flew an F-16 fighter jet with artificial intelligence handling the controls, including maneuvers against a human-piloted aircraft. The program is testing whether AI can safely fly combat aircraft with a person overseeing rather than steering.

**What this means**
Autonomous systems are moving from demos into real, high-stakes machines. For anyone watching how AI gets regulated — lawyers, policymakers, safety officers — military aviation is becoming an early test of how much control we hand to software and how we keep a human accountable.

Source: [DARPA ↗](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)

---
## Quick Hits

### Startups Urge Washington Not to Cut Off Chinese Open AI Models

A group of U.S. startup founders is asking the government not to block access to freely downloadable AI models made in China, arguing that many American companies now build on top of them. It sets up a policy clash between national-security concerns and the businesses that rely on cheap, open models.

Source: [Politico ↗](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

### Report: AI Companies Are Hiding a Lot of Debt

A new report argues that some of the biggest names in AI are keeping large amounts of debt off their main balance sheets, often through financing tied to data centers and chips. If accurate, it means the true cost of the AI build-out is harder to see than the headline numbers suggest — worth watching for anyone tracking the industry's finances.

Source: [Futurism ↗](https://futurism.com/artificial-intelligence/ai-companies-hide-debt-off-balance-sheet)

### GitHub's Dependabot Now Waits Before Pushing Software Updates

GitHub changed its automated update tool, Dependabot, to wait three days by default before recommending a new version of a software component. The pause gives maintainers and security researchers time to catch problems in a fresh release before it flows automatically into everyone's projects.

Source: [GitHub Blog ↗](https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/)

### Astronomers May Have Found the First Exomoon

Using ground-based telescopes, scientists reported possible signs of a moon orbiting a planet in another solar system — something that has never been confirmed before. It is still a candidate, not a certainty, but if it holds up it opens a new frontier for studying distant worlds.

Source: [ESO ↗](https://www.eso.org/public/news/eso2610/)

---
## Under the Hood

### Running 4-Bit Image Models Directly in Diffusers

**What happened**
Hugging Face added native support for Nunchaku, a method that squeezes image-generation models down to 4-bit precision so they run faster and use far less memory. It now loads directly inside Diffusers, the popular library for running these models, without extra setup.

**Why it matters**
Compressing a model to 4 bits means storing each number with a quarter of the usual detail — the trade is a little quality for a big drop in memory and cost. This is what lets heavy image models run on ordinary consumer graphics cards instead of expensive data-center hardware.

Source: [Hugging Face ↗](https://huggingface.co/blog/nunchaku-diffusers)

### Grabette: Recording Robot Training Data With Your Own Hands

**What happened**
Hugging Face released Grabette, an open system for capturing how a human hand manipulates objects and turning that into a dataset for training robots. You record a motion, then process it in the browser into data a robot can learn from.

**Why it matters**
The hardest part of robotics is rarely the model — it's getting enough real examples of how to grasp and move things. Cheap, open tools for collecting that data lower the barrier for researchers and hobbyists who don't have a lab full of robot arms.

Source: [Hugging Face ↗](https://huggingface.co/blog/grabette)

---
**Fun fact:** Astronomers think they may have spotted the first known moon orbiting a planet outside our solar system.

*Daily tech digest for curious professionals. AI news that affects your work.*