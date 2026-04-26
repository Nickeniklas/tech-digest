# Daily Tech Digest — Sunday, April 26 2026

> OpenAI says its coding benchmark no longer measures what it claims to—and it matters if you're evaluating AI coding tools.

---
## OpenAI Questions Its Own Coding Benchmark

**What happened**
OpenAI published an analysis explaining why SWE-bench Verified—a widely-used test for measuring AI coding capabilities—no longer accurately reflects how well AI models can actually code. The benchmark has become easier as models improve, making it unreliable for comparing today's frontier tools.

**What this means**
If you've been using SWE-bench scores to evaluate AI coding assistants for your team—whether you're a manager picking tools or a developer choosing what to trust—those numbers may be misleading you now. Benchmarks need to evolve as AI gets better, or they stop telling you anything useful. This is a rare moment of transparency: OpenAI is admitting one of the standard measures in the industry isn't working anymore.

Source: [OpenAI ↗](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

---
## Quick Hits

### Amateur Solves 60-Year-Old Math Problem Using ChatGPT

A non-professional mathematician used ChatGPT to help solve an Erdős problem—a type of puzzle that has stumped professional researchers for decades. This is a tangible example of AI amplifying human problem-solving beyond what experts alone could do, though the mathematician still brought the core insight.

Source: [Scientific American ↗](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/)

### Git 2.54 Released with Performance Improvements

The open-source Git project released version 2.54 with notable features and performance improvements. GitHub highlighted the update for developers who want the latest version control capabilities.

Source: [GitHub Blog ↗](https://github.blog/open-source/git/highlights-from-git-2-54/)

### GitHub Improves Deployment Safety with eBPF

GitHub shared how it uses eBPF (extended Berkeley Packet Filter)—a low-level Linux technology—to detect and prevent circular dependencies in its deployment tooling. This is infrastructure work that makes GitHub itself more reliable when you push code.

Source: [GitHub Blog ↗](https://github.blog/engineering/infrastructure/how-github-uses-ebpf-to-improve-deployment-safety/)

---
## Under the Hood

### Microsoft Porting TypeScript to Go Natively

**What happened**
Microsoft opened a staging repository for a native port of TypeScript written in Go instead of the current JavaScript/Node implementation. This is early-stage work, but it signals intent to rewrite one of the most widely-used programming languages in a faster, more manageable system language.

**Why it matters**
TypeScript is used by millions of developers daily. A Go-based implementation could make the language significantly faster to run and easier to maintain, but the migration is a multi-year effort. This affects anyone who builds with TypeScript, though real-world impact is still years away.

Source: [GitHub ↗](https://github.com/microsoft/typescript-go)

### Open Infrastructure for AI Agents That Control Desktops

**What happened**
A project called CUA released open-source infrastructure for building and training AI agents that can operate full desktop environments (Windows, macOS, Linux). The toolkit includes sandboxes, SDKs, and benchmarks so developers can train agents that interact with computers the way humans do—clicking, typing, navigating windows.

**Why it matters**
Computer-use agents (AI that can take control of your desktop) are becoming a real research area. Open-source infrastructure lowers the barrier for developers and researchers to experiment with this capability. This is the foundation layer that could enable new kinds of automation, though safety and trust are still open questions.

Source: [GitHub ↗](https://github.com/trycua/cua)

---
**Fun fact:** An amateur mathematician just solved a 60-year-old math puzzle with ChatGPT's help—the kind that stumped professionals for decades.

*Daily tech digest for curious professionals. AI news that affects your work.*