# Daily Tech Digest — Sunday, November 22 2026

> A computer has now checked, step by step, the claimed proof of one of math's most famous unsolved problems — and it's a reminder of how machines are starting to verify human work, not just produce it.

---
## The Riemann Hypothesis proof gets a computer-checked verification

**What happened**
Previously covered on 2026-11-21: mathematician Levent Alpöge posted a claimed proof of the Generalized Riemann Hypothesis, a century-old question about prime numbers. Since then, the Lean community has published a verification of the proof in Lean — software that checks every logical step of a proof mechanically — and the verification files are hosted at MIT.

**What this means**
A claimed proof this big would normally take experts months or years to check by hand; a machine check means the logic has been tested line by line. It's a clear example of a broader shift you'll see in your own field: computers checking expert work, not just generating it.

Source: [Lean Community Blog ↗](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

---
## Quick Hits

### Two AI providers disclose incidents with customer prompts

OpenRouter, a service that routes AI requests to many model providers, published a post on data processing incidents at those providers, and Together.ai disclosed that some customer prompts leaked in June and July 2026. If you paste client or company material into AI tools, it's worth knowing which provider actually handles your requests.

Source: [Together.ai ↗](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)

### A pill for pancreatic cancer is called the biggest breakthrough in decades

The Guardian reports that daraxonrasib, a pill to treat pancreatic cancer, is being hailed as the biggest advance against the disease in decades. Pancreatic cancer is among the hardest cancers to treat, so the news drew wide attention well beyond the medical world.

Source: [The Guardian ↗](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)

### Git fixes six security flaws — update your tools

Git, the version-control system behind almost all software projects, released updates for six security vulnerabilities. They affect everyday operations such as copying a project, merging changes, and importing data, so if your team uses Git, ask IT to make sure it's updated.

Source: [GitHub Blog ↗](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/)

### Pandex gives AI agents direct access to official European law

Pandex is a new service that lets AI agents look up official European legal texts through MCP, a standard way of connecting AI tools to outside data. For lawyers and compliance teams, that means AI assistants can cite the actual source text instead of relying on memory.

Source: [Pandex ↗](https://www.pandex.io)

---
## Under the Hood

### LLMs can read and write programs straight from a hex dump

**What happened**
A blog post shows large language models reading and writing executable files byte by byte from a hex dump — the raw numbers a computer actually runs — without any source code or programming language in between.

**Why it matters**
It suggests models understand machine code more deeply than expected, which matters for reverse engineering, security research, and analysing old software with no surviving source. It also means malware analysis — and malware writing — get easier.

```python
# Show the first 64 bytes of a program as a hex dump
with open("program.bin", "rb") as f:
    data = f.read(64)
for i in range(0, len(data), 16):
    print(f"{i:04x}: {data[i:i+16].hex(' ')}")
```

Source: [sgiannopoulos.github.io ↗](https://sgiannopoulos.github.io/blog/machine-code-programming/)

### Inkling 2 Mini squeezed into 5.4 GB of memory

**What happened**
Previously covered on 2026-11-21: Thinking Machines released Inkling 2 Mini, an open model built to run locally. Since then, a developer has published a compressed (quantized) version that runs in just 5.4 GB of memory — the model has about 26 billion parameters in total but uses only 3 billion for each word it processes.

**Why it matters**
5.4 GB fits on many ordinary laptops, so a capable text-and-image model can run fully offline, keeping your data on your own machine. Quantization trades a little accuracy for a much smaller memory footprint.

Source: [GitHub ↗](https://github.com/ShinMegamiBoson/lookatmyquant)

---
**Fun fact:** An AI model can now read and write working programs as raw bytes — no programming language needed.

*Daily tech digest for curious professionals. AI news that affects your work.*