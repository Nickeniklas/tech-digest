# Daily Tech Digest — Monday, August 3 2026

> Alibaba has a new top-tier coding model, Californians can now force data brokers to delete their records, and someone squeezed a language model onto a 1970s home-computer chip.

---
## Alibaba's Qwen Team Releases Qwen3.8-Max

**What happened**
Alibaba's Qwen team released Qwen3.8-Max, which it positions as its strongest model yet for writing code and for "cowork" — working alongside a person on multi-step tasks rather than answering one question at a time.

**What this means**
The list of models that can credibly handle real work keeps growing, and Chinese labs are now a standing part of it rather than a curiosity. If your organisation is choosing an AI tool, the practical effect is more competition on price and fewer reasons to lock into one vendor.

Source: [Qwen ↗](https://qwen.ai/blog?id=qwen3.8)

---
## Quick Hits

### Californians Can Now Force Data Brokers to Delete Their Data

California's DROP system — one request that reaches the data brokers holding your personal information — became enforceable on August 1. Californians can file a single deletion request instead of chasing hundreds of companies individually. If you work in marketing, sales, or anywhere that buys contact lists, expect the lists to start shrinking.

Source: [NBC 7 San Diego ↗](https://www.nbcsandiego.com/nbc-7-responds-2/californians-data-deletion-requests-drop-become-enforceable-aug-1/4054771/)

### A Working Example of GitHub's Stacked Pull Requests

Previously covered on 2026-07-31: GitHub put stacked pull requests — splitting one large change into a chain of smaller reviewable pieces — into public preview. GitHub has now published a walkthrough of someone using the feature end to end to modernise an old codebase. It is the clearest picture yet of what the workflow actually looks like day to day.

Source: [GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/)

### Why People Get Attached to Their Tools

Stack Overflow published an argument that developers cling to particular tools because a tool people have used for years encodes trust — you know exactly how it behaves when things go wrong. It is a useful frame for anyone being asked to swap a familiar tool for an AI-assisted one: resistance is usually about predictability, not stubbornness.

Source: [Stack Overflow Blog ↗](https://stackoverflow.blog/2026/07/29/developers-are-attached-to-tools-because-tools-encode-trust/)

### Thinking Machines Publishes a Model Called Inkling

The AI lab Thinking Machines released a model named Inkling on Hugging Face, the site where open models are shared and downloaded. Details are thin so far, but it is another lab choosing to publish rather than keep its work behind an API.

Source: [Hugging Face ↗](https://huggingface.co/blog/thinkingmachines-inkling)

---
## Under the Hood

### Dependabot Now Waits Three Days Before Suggesting an Update

**What happened**
Dependabot is the GitHub service that automatically opens a pull request when a piece of third-party code your project depends on publishes a new version. GitHub changed the default so those version-update pull requests now wait three days after a release, giving maintainers and security researchers a window to spot problems in a release before it lands in your code. Security fixes are exempt and still go out immediately.

**Why it matters**
The old default made every project an early adopter by accident, including the bad releases. Three days is short enough that you stay current and long enough that most withdrawn or compromised releases get caught first — a small default change that quietly shifts risk off thousands of repositories.

Source: [GitHub Blog ↗](https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/)

### A Language Model Running on a 6502

**What happened**
A developer got an autoregressive language model — the same basic design as the chatbots you use, generating one word at a time and feeding each one back in — running on the 6502, the 8-bit processor from the 1970s that powered the Apple II, the Commodore 64 and the NES. It is a demonstration rather than a product: the machine has a few kilobytes of memory and runs at a fraction of a modern phone's speed.

**Why it matters**
The interesting part is what it proves about the design rather than the hardware. The loop below is the whole idea behind text generation, and it is small enough to fit on a chip from fifty years ago — the intelligence comes from the size of the model's weights, not from any complexity in the surrounding machinery.

```python
# The entire generation loop, in five lines
tokens = [start_token]
for _ in range(50):
    scores = model(tokens)        # score every possible next token
    next_token = sample(scores)   # pick one
    tokens.append(next_token)     # feed it back in
print(detokenize(tokens))
```

Source: [Matt Beton ↗](https://mattbeton.com/blog/bitnet-6502.html)

---
**Fun fact:** A working language model now runs on the 8-bit chip from the Commodore 64.

*Daily tech digest for curious professionals. AI news that affects your work.*