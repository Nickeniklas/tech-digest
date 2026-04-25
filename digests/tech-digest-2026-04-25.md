# Daily Tech Digest — Saturday, April 25 2026

> Microsoft rewrites TypeScript in Go for native speed, HuggingFace ships an open-source ML intern agent, and two sharp dev-tools round out a week of practical releases.

**Today's pick:** The TypeScript-Go port isn't a side project — Microsoft is serious about erasing compile-time pain from large codebases. If benchmarks hold in real monorepos, this reshapes how teams think about CI and build tooling for the next decade.

---
**Fun fact:** The Go port of the TypeScript compiler is so fast it can type-check itself before most developers finish reading the changelog.

---
## Microsoft Ports the TypeScript Compiler to Go — 🛠️ Dev Tools

**WHAT HAPPENED**
[microsoft/typescript-go](https://github.com/microsoft/typescript-go) is a native Go port of the TypeScript compiler. Early results show type-checking and compilation times dropping dramatically on large codebases — this is a staged repo, meaning Microsoft is building toward an official release.

**WHY IT MATTERS**
TypeScript build time is the hidden tax on every large JS project. A native-compiled Go implementation sidesteps the V8 overhead that makes `tsc` slow at scale, which means faster CI, faster editor feedback, and less waiting in monorepos.

**TRY IT**
```bash
git clone https://github.com/microsoft/typescript-go
cd typescript-go
git checkout main
go build ./...
# Run the experimental compiler against your own project:
./built/local/tsgo --project path/to/tsconfig.json
```

Source: [GitHub Trending ↗](https://github.com/microsoft/typescript-go)

---
## HuggingFace Open-Sources an ML Engineer That Trains Its Own Models — 🤖 AI

**WHAT HAPPENED**
[huggingface/ml-intern](https://github.com/huggingface/ml-intern) is an open-source ML agent that reads research papers, spins up training runs, and publishes the resulting models — the full research-to-deployment loop automated.

**WHY IT MATTERS**
Closing the loop between reading a paper and running the experiment has been a bottleneck for small ML teams. This is early, but it signals a shift toward agent-assisted research workflows that could dramatically compress iteration cycles.

**THE TAKE**
This is research infrastructure, not production tooling yet. Worth watching closely if you run ML pipelines — the underlying loop (plan → train → evaluate → publish) is exactly what teams wire together manually today.

Source: [GitHub Trending ↗](https://github.com/huggingface/ml-intern)

---
## Google OSV-Scanner: One Tool for Vulnerability Scanning Across All Ecosystems — 🛠️ Dev Tools

**WHAT HAPPENED**
[google/osv-scanner](https://github.com/google/osv-scanner) is a Go-based vulnerability scanner that queries the [OSV database](https://osv.dev) to surface known CVEs across your project's lockfiles — covering Go, Python, Rust, npm, and more.

**WHY IT MATTERS**
Most teams run separate scanners per language — `npm audit` here, `pip-audit` there. OSV-Scanner handles polyglot repos in a single pass, making it practical for monorepos that your current security tooling can't cover consistently.

**TRY IT**
```bash
go install github.com/google/osv-scanner/cmd/osv-scanner@latest

# Scan a specific lockfile
osv-scanner --lockfile ./package-lock.json
osv-scanner --lockfile ./requirements.txt

# Recursive scan of an entire repo
osv-scanner -r ./
```

Source: [GitHub Trending ↗](https://github.com/google/osv-scanner)

---
## DeepSeek Releases DeepEP: Expert-Parallel Communication for MoE Models — 🤖 AI

**WHAT HAPPENED**
[deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) is an open-source communication library purpose-built for expert-parallel inference and training of Mixture-of-Experts models across multi-GPU and multi-node setups.

**WHY IT MATTERS**
MoE architectures need efficient all-to-all communication that standard NCCL handles poorly at scale — DeepEP is the missing primitive. Infrastructure teams building or serving large MoE models now have a battle-tested starting point from the team that shipped DeepSeek.

**THE TAKE**
Application developers won't touch this directly, but providers who adopt it pass the efficiency gains downstream as lower inference costs. If you're building ML infra for MoE models, this is the first serious open-source baseline to benchmark against.

Source: [GitHub Trending ↗](https://github.com/deepseek-ai/DeepEP)

---
## Claude Context MCP Gives Claude Code Semantic Search Over Your Entire Codebase — 🛠️ Dev Tools

**WHAT HAPPENED**
[zilliztech/claude-context](https://github.com/zilliztech/claude-context) is an MCP server that indexes your codebase and exposes semantic code search to Claude Code, letting the agent find relevant files without you manually specifying paths.

**WHY IT MATTERS**
Claude Code's context window is finite — in large repos you're constantly pre-selecting files to feed in. This MCP handles retrieval automatically, giving Claude Code genuine whole-repo awareness rather than the local slice you happened to open.

**TRY IT**
```bash
git clone https://github.com/zilliztech/claude-context
cd claude-context && pip install -e .

# Index your codebase
claude-context index /path/to/your/project

# Add to .claude/mcp.json:
# {"mcpServers": {"claude-context": {"command": "claude-context", "args": ["serve"]}}}
# Then in Claude Code: ask about any file, function, or pattern
```

Source: [GitHub Trending ↗](https://github.com/zilliztech/claude-context)

---
*Daily digest for developers. AI, dev tools, and the occasional hardware drop that actually matters.*