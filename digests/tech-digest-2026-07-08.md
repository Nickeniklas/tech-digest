# Daily Tech Digest — Wednesday, July 8 2026

> A hidden backdoor turns up in popular home routers, the EU makes driver-watching cameras mandatory, and free AI voice software now runs on an ordinary laptop.

---
## A Hidden Backdoor Is Lurking in Popular Home Routers

**What happened**
Security researchers at Carnegie Mellon's CERT Coordination Center reported that several firmware versions of Tenda routers ship with a hidden, built-in login that lets an outsider bypass the normal password and take control of the device.

**What this means**
If you use a Tenda router at home or in a small office, someone on your network — and in some setups over the wider internet — could take it over without ever knowing your password, then snoop on or reroute your traffic. Check your model, install any firmware update, and if none exists, consider replacing it.

Source: [CERT Coordination Center ↗](https://kb.cert.org/vuls/id/213560)

---
## Quick Hits

### Every New EU Car Will Watch the Driver

New rules mean every car sold in the European Union must now include a camera or sensor system that monitors the driver for signs of distraction or drowsiness. Safety groups say it could cut crashes, while privacy advocates worry about cameras pointed at people inside their own cars.

Source: [All About Cookies ↗](https://allaboutcookies.org/eu-mandatory-distracted-driver-system)

### Free, High-Quality AI Voice That Runs on a Laptop

A developer showed how to run Kokoro, an open text-to-speech model, entirely on an ordinary computer's processor — no expensive graphics card and nothing sent to the cloud. For anyone who wants a natural-sounding AI narrator for audio, videos, or accessibility without a subscription, it's a genuinely usable free option.

Source: [Ariya Hidayat ↗](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/)

### Open-Source Collaboration Keeps Speeding Up Worldwide

GitHub's latest Innovation Graph, its running snapshot of global software activity, shows developer communities growing and collaborating across borders faster than ever. It's a reminder that much of the technology quietly running your workplace tools is built in the open by people around the world.

Source: [GitHub Blog ↗](https://github.blog/news-insights/policy-news-and-insights/q1-2026-innovation-graph-update-open-source-collaboration-is-accelerating-worldwide/)

### Deploying an AI Model Just Got a One-Click Shortcut

Hugging Face and Amazon added a way to move an AI model from Hugging Face's library into Amazon's cloud tools with a single click, skipping much of the fiddly setup. It won't change your day directly, but it's another sign of how quickly companies can now put AI features into the products you use.

Source: [Hugging Face ↗](https://huggingface.co/blog/amazon/one-click-to-sagemaker-studio)

---
## Under the Hood

### Git 2.55 Ships With Speed and Quality-of-Life Upgrades

**What happened**
The open-source Git project — the version-control system that underpins almost all modern software development — released version 2.55. GitHub's rundown highlights performance work and refinements to everyday commands rather than headline new features.

**Why it matters**
Git sits under the hood of nearly every software team, so incremental speedups and smoother commands quietly save time for millions of developers. If you work alongside engineers, this is the kind of invisible plumbing update that keeps their tools fast.

```python
git switch -c my-feature
git add .
git commit -m "Try Git 2.55"
git push -u origin my-feature
```

Source: [GitHub Blog ↗](https://github.blog/open-source/git/highlights-from-git-2-55/)

### AI Turns Up Real Bugs in Cloudflare's Cryptography Code

**What happened**
A security write-up walks through how AI tools were pointed at Circl, an open-source cryptography library from Cloudflare, and helped surface genuine flaws in code that is supposed to be extremely carefully written. The post details what the AI found and how the issues were confirmed.

**Why it matters**
Cryptography code is among the hardest to get right, and bugs there can undermine security everywhere it's used. Showing that AI can act as an extra reviewer — not a replacement for experts, but a tireless second pair of eyes — points to how code auditing may work going forward.

Source: [zkSecurity ↗](https://blog.zksecurity.xyz/posts/circl-bugs/)

---
**Fun fact:** A pure-Python program rediscovered Kepler's law of planetary motion from just eight data points.

*Daily tech digest for curious professionals. AI news that affects your work.*