# Daily Tech Digest — Saturday, August 15 2026

> Google is working on AI that can process your files without ever being able to read them.

---
## Google Is Making AI That Works on Data It Cannot Read

**What happened**
Google published how it is using homomorphic encryption — a method that lets a computer run calculations on encrypted data without ever unlocking it — to make private AI features practical in real products rather than just in research papers.

**What this means**
It points toward AI tools you could use on genuinely confidential material — client files, medical notes, HR records — without handing the readable contents to someone else's server. For lawyers, clinicians and anyone bound by confidentiality rules, that is often the difference between an AI tool being permitted at work and being off-limits.

Source: [Google ↗](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)

---
## Quick Hits

### Where Open AI Models Actually Stand This Summer

Hugging Face published its half-yearly review of open models — the ones anyone can download and run on their own machines. Its main observations: attention is not the same as adoption, Alibaba's Qwen has become the community's default starting point, small models remain the practical choice for real work, and agents rather than people are increasingly the ones using them.

Source: [Hugging Face ↗](https://huggingface.co/blog/state-of-open-models-summer-2026)

### Firefox Is Now the Last Major Browser Where uBlock Origin Still Works

Chrome and the other Chromium-based browsers have finished phasing out the extension format uBlock Origin depends on, leaving Firefox as the only major browser where the ad blocker still runs in full. This comes days after the project said it was giving up on keeping ads off Facebook. If you rely on it, your browser choice is now the deciding factor.

Source: [PCWorld ↗](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html)

### A New Open Coding Model Arrives With Security Skills Attached

Z.ai released GLM-5.3, which it presents as frontier-level at writing code, and says cyber capabilities emerged alongside that skill. The same ability that finds and patches security holes can be pointed at finding and exploiting them, which is why model releases are increasingly a security question as well as a productivity one.

Source: [Z.ai ↗](https://z.ai/blog/glm-5.3)

### What 50 Open Source Projects Learned About Security in the AI Era

GitHub wrote up the fourth round of its Secure Open Source Fund, where 50 projects combined AI-assisted workflows, maintainer expertise, security tooling and funding to harden their code. Almost every company runs on this kind of unpaid infrastructure, so what these maintainers fix quietly ends up in software you use.

Source: [GitHub Blog ↗](https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/)

---
## Under the Hood

### One Loop From Robot Demonstration to Deployed Policy

**What happened**
Amazon and Hugging Face described a single pipeline for training robots: record a human demonstration straight into a cloud storage bucket, store it with byte-level deduplication so repeated frames are not saved twice, train by streaming the data from the Hub instead of downloading a copy, then deploy the resulting policy and feed its new recordings back into the same loop.

**Why it matters**
Robot training data is enormous and highly repetitive, and the usual bottleneck is not the model but moving terabytes of video around. Deduplicating at the byte level and streaming during training removes the copy step entirely, which is what makes a continuous record-train-deploy loop affordable for a small team.

Source: [Hugging Face ↗](https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop)

### RustDesk Adds Unattended Remote Access on Wayland

**What happened**
RustDesk, the open source alternative to TeamViewer, now supports true unattended remote access on Wayland — the display system that has been replacing the decades-old X11 on Linux desktops. Until now, connecting to an unattended Wayland machine generally required someone sitting at it to approve the session.

**Why it matters**
Wayland deliberately isolates applications from each other, which blocks the screen capture and keyboard injection that remote-desktop tools rely on. Working around that without reopening the security hole is the hard part, and it is what has kept Linux support desks pinned to X11.

Source: [RustDesk ↗](https://rustdesk.com/blog/unattended-remote-access-wayland/)

---
**Fun fact:** A 31-year-old Easter egg was just unearthed inside the Sega game Ecco the Dolphin.

*Daily tech digest for curious professionals. AI news that affects your work.*