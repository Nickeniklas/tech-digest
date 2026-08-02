# Daily Tech Digest — Sunday, August 2 2026

> Anthropic's new top-tier model gets close to its most capable one at half the price — the clearest sign this week that the expensive end of AI keeps getting cheaper.

---
## Anthropic Releases Claude Opus 5

**What happened**
Anthropic released Claude Opus 5, the newest model in its Opus tier. It is aimed at tasks that run for a long time without someone watching over them, and Anthropic says it comes close to the intelligence of its most capable model, Claude Fable 5, at half the price.

**What this means**
The pattern keeps repeating: what cost a premium six months ago costs half as much now. If you have held off on AI tools because the good ones were too expensive for real work — reviewing a long contract, working through a research task over hours rather than minutes — that calculation keeps moving in your favour.

Source: [Anthropic ↗](https://www.anthropic.com/news/claude-opus-5)

---
## Quick Hits

### ByteDance Releases Seedance 2.5

ByteDance published Seedance 2.5, an update to its AI video model built around generating a shot in one take and using reference images to keep characters and settings consistent. Consistency has been the weak point of AI video — faces and props drift between clips — so that is the part of the problem worth watching.

Source: [ByteDance Seed ↗](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

### China Starts Making Its Own Advanced Chipmaking Machines

China has begun producing home-grown immersion deep-ultraviolet lithography machines — the equipment that prints circuits onto silicon — according to a source cited by Reuters. Only a handful of companies outside China can build these, and export controls have kept them out of Chinese factories.

Source: [Reuters ↗](https://www.reuters.com/world/china/china-starts-production-home-grown-immersion-duv-chipmaking-tools-source-2026-07-28/)

### AI Financial Advice Holds Up Better Than Expected

MIT Sloan looked at how well AI assistants answer personal finance questions and found the advice largely holds up — provided you ask specific questions rather than vague ones. The difference between a useful answer and a generic one comes down to how much of your actual situation you put in the question.

Source: [MIT Sloan ↗](https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions)

### US Warns of Attacks on Water Utility Controllers

CISA, the US cybersecurity agency, issued an alert about attackers targeting the programmable controllers that run water treatment and distribution equipment. These are small industrial computers that were never designed to sit on the public internet, and plenty of them still do.

Source: [Censys ↗](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)

---
## Under the Hood

### TLS 1.2's Oldest Key Exchange Methods Are Officially Deprecated

**What happened**
The IETF published RFC 10015, which formally deprecates obsolete key exchange methods in TLS 1.2 and DTLS 1.2 — the handshake step where a browser and a server agree on a shared secret before any encryption starts. Deprecation is not removal: the methods still function, but the standards body is now telling implementers to stop offering them.

**Why it matters**
Most of what is on that list lacks forward secrecy, which means a server key stolen years from now could decrypt traffic captured today. TLS 1.3 left these methods out at design time; this closes the same door on the older version that much of the long tail of the internet still runs.

Source: [RFC Editor ↗](https://www.rfc-editor.org/rfc/rfc10015.html)

### A Soundness Bug in Lean's Proof Kernel, Written Up in Full

**What happened**
Leonardo de Moura published a postmortem for bug #14576 in the kernel of Lean, the proof assistant — the small trusted core that checks every proof the system accepts. A soundness bug there means the checker can be talked into accepting something false, which is the one category of bug a proof assistant cannot live with.

**Why it matters**
Lean is increasingly used to verify mathematics and, in a few places, real software. That whole arrangement rests on the kernel being small enough to audit and trust, so the useful part of a postmortem like this is less the bug itself than what it shows about how that core gets scrutinised.

Source: [Leonardo de Moura ↗](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/)

---
**Fun fact:** A 15-year-old designed and built a cycloidal gearbox, then posted the whole thing on GitHub.

*Daily tech digest for curious professionals. AI news that affects your work.*