# Daily Tech Digest — Wednesday, September 23 2026

> OpenAI's GPT-6 is here, and one version of it cracked a coded message that had gone unsolved for over twenty years.

---
## OpenAI released GPT-6 — and one version broke a cipher nobody had solved since 2005

**What happened**
OpenAI released GPT-6 in two versions, Sol and Luna. Separately, a GPT-6 model called Astra was used to break an Enigma-encrypted message that had resisted codebreakers since 2005.

**What this means**
The tools you already use for drafting, summarising and research will get another step more capable over the coming weeks as GPT-6 reaches the products built on OpenAI's models. The Enigma result is the more telling part: these systems are now good at grinding through problems that used to need a specialist and a great deal of patience.

Source: [OpenAI ↗](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

---
## Quick Hits

### Anthropic's new Opus costs 40% less to run

Anthropic released Claude Opus 5.5, which it says performs at the level of Claude Fable 5.1 on most work while costing 40% less to run than Opus 5. Cheaper models at the same quality usually reach you as lower prices or more generous limits in the tools built on top of them.

Source: [Anthropic ↗](https://www.anthropic.com/claude-opus-5-5)

### The Pentagon says overreliance on AI contributed to a strike on an Iranian school

A Bloomberg investigation reports the Pentagon's finding that leaning too heavily on AI played a part in a missile strike that hit a school in Iran. It is one of the clearest official acknowledgements yet that automated advice carries real consequences when the people using it stop questioning the output.

Source: [Bloomberg ↗](https://www.bloomberg.com/graphics/2026-iran-school-attack/)

### A WordPress flaw can let strangers run code on your site

WordPress published a security advisory for a path traversal bug that needs no login to exploit and can lead to remote code execution under certain conditions. If your team runs anything on WordPress — a blog, a campaign site, a client's homepage — this is a same-day update.

Source: [WordPress Security Advisory ↗](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp)

### Apple is putting ads in iOS that won't go away

TechRadar reports that recent iOS releases show persistent promotional prompts for Apple services, and that users are finding them difficult to dismiss for good. Worth knowing if you manage phones for a team: the prompts appear on the same devices you hand to staff.

Source: [TechRadar ↗](https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy)

---
## Under the Hood

### Transformers now loads llama.cpp's compressed models directly

**What happened**
Hugging Face's transformers library can now read GGUF files — the compressed model format llama.cpp popularised — without converting them first, and reuses ggml's Metal kernels so Apple hardware keeps its speed. The same quantized file you run in llama.cpp can be loaded straight into Python.

**Why it matters**
Quantized GGUF files are how most people run models on their own laptop. Until now you chose between a fast local runtime and the Python ecosystem you actually build in; this removes that choice.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "bartowski/Llama-3.2-3B-Instruct-GGUF"
gguf = "Llama-3.2-3B-Instruct-Q4_K_M.gguf"

tok = AutoTokenizer.from_pretrained(repo, gguf_file=gguf)
model = AutoModelForCausalLM.from_pretrained(repo, gguf_file=gguf)
```

Source: [Hugging Face ↗](https://huggingface.co/blog/transformers-llama-cpp-quants)

### The standard behind your work login is called a fractal of bad design

**What happened**
Trail of Bits published a long critique of SAML, the protocol behind most "sign in with your work account" buttons. Its argument: SAML depends on XML signatures, a scheme where the same document can be read two different ways by the part that checks the signature and the part that reads the contents.

**Why it matters**
SAML underpins single sign-on at most large organisations. When a protocol is this hard to implement correctly, the bugs that result tend to be authentication bypasses — an attacker signing in as someone else, rather than merely crashing something.

Source: [Trail of Bits ↗](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/)

---
**Fun fact:** Microsoft killed off FoxPro in 2007. Someone has now brought it back anyway.

*Daily tech digest for curious professionals. AI news that affects your work.*