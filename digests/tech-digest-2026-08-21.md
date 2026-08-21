# Daily Tech Digest — Friday, August 21 2026

> GitHub explains the outage that stalled software teams last week, and a call goes out to rescue rare books before AI companies cut them apart.

---
## GitHub Explains the August 17 Outage and What It Is Changing

**What happened**
GitHub published an account of the outage that degraded its services on August 17, along with the reliability work it is committing to next. The company also counted eight separate incidents in July, so this write-up lands on top of an already uneven few months.

**What this means**
GitHub is where most of the world's software is stored and shipped, so when it stops, your company's bug fixes, app updates, and website changes stop with it. If your product team went quiet last week without a clear explanation, this is the reason, and the post is a fair thing to send them when you ask what happens next time.

Source: [GitHub Blog ↗](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/)

---
## Quick Hits

### AI Companies Are Cutting Books Apart to Scan Them

Anna's Archive argues that AI companies are buying physical books and destroying them in the process of digitising them, since slicing the spine off is the fastest way to feed pages through a scanner. It is calling for rare and hard-to-replace books to be scanned carefully first, before the only copies end up in a shredder. For anyone who works with archives, collections, or reference material, the point is that a copy in a training set is not the same thing as a copy on a shelf.

Source: [Anna's Archive ↗](https://annas-archive.gl/blog/physical-destruction.html)

### AliExpress Is Fingerprinting Visitors Through Their Audio Hardware

A developer traced a strange bug in their Bluetooth headphones, which kept dropping the connection to a second device, back to AliExpress running silent audio fingerprinting in the background of its web pages. Fingerprinting builds a quiet identifier for your device from tiny quirks in how it handles sound, so you can be recognised without a cookie or a login. The unusual part is that the tracking was noticeable at all, because it broke something the user could actually feel.

Source: [Laserphile ↗](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html)

### A Malicious Software Package Ran Its Payload Before Anyone Pressed Run

Security researchers at SafeDep found a package in Rust's public library index that executes hostile code while software is being built, not when it is later run. That timing matters: developers often assume they are safe as long as they have not launched anything yet. It is the same category of supply chain problem that has been hitting open source package registries for years, arriving in a language whose users mostly thought they were past it.

Source: [SafeDep ↗](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/)

### A Small Model That Plays Piano With You

A developer trained a 125-million-parameter model that autocompletes piano playing and runs entirely on the device rather than in a data centre. That is a tiny model by current standards, thousands of times smaller than the ones behind the chatbots you use at work. It is a useful reminder that plenty of genuinely handy AI does not need a subscription or an internet connection.

Source: [simedw.com ↗](https://simedw.com/2026/08/20/midi-autocomplete/)

---
## Under the Hood

### Mojo Is Now Open Source

**What happened**
Modular has opened the source code of Mojo, the programming language it built to write high-performance AI code with Python-like syntax. Until now the language was developed in the open only in the sense that you could use it; the implementation itself was closed, which made it a hard bet for anyone wanting to build on top of it long term.

**Why it matters**
The gap Mojo aims at is real: the AI world writes its glue in Python and its fast paths in C++ or CUDA, and moving between the two is where a lot of engineering time goes. Whether Mojo closes that gap now depends on a community forming around it, which is exactly what opening the source is for.

Source: [Modular ↗](https://www.modular.com/blog/mojo-open-source)

### Draft Models That Make Inference Up to 3.2x Faster

**What happened**
Liquid AI released DSpark draft model checkpoints for three models in its LFM2.5 family: LFM2.5-1.2B-Instruct, LFM2.5-2.6B, and LFM2.5-8B-A1B. They add speculative decoding, where a small fast model guesses the next several words and the big model only has to check the guess instead of producing every word itself. Liquid AI reports up to 3.2x faster inference on both CPU and GPU while keeping output quality on par with the original models.

**Why it matters**
Speculative decoding is one of the few speed tricks that costs you nothing in output quality, because the large model still has the final say on every token. For anyone running models on their own hardware, especially on CPUs where every token is expensive, a 3x speedup changes what is practical to run locally.

Source: [Hugging Face ↗](https://huggingface.co/blog/LiquidAI/lfm25-dspark)

---
**Fun fact:** A 125-million-parameter model, small enough to run on your own device, can now finish your piano phrases.

*Daily tech digest for curious professionals. AI news that affects your work.*