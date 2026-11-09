# Daily Tech Digest — Monday, November 9 2026

> Microsoft's Outlook.com is reportedly turning away email from domains that skip a basic security setting, so your newsletters and invoices could be disappearing without anyone noticing.

---
## Outlook.com is quietly rejecting email from domains without DMARC

**What happened**
A widely shared report from email provider MailRoute says Outlook.com is rejecting messages from sending domains that don't publish DMARC, a short DNS record that tells inboxes how to check that an email really comes from you. Senders aren't clearly warned when it happens.

**What this means**
If your company, school or small business sends email from its own domain, ask whoever manages it whether DMARC is set up. Marketers sending campaigns and freelancers sending invoices are the most likely to lose messages without knowing.

Source: [MailRoute ↗](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc)

---
## Quick Hits

### Goldman Sachs is pulling Claude Code from its bankers and traders

A report says Goldman Sachs is taking Anthropic's AI coding assistant, Claude Code, away from staff in its banking and trading teams. It's a sign that large, heavily regulated employers are still deciding who should get powerful AI tools at work, so expect your own company's rules to keep shifting.

Source: [The State of AI ↗](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)

### Anthropic maps out possible futures for an AI economy

Anthropic published 'Scenarios for our economic future', which starts from a plain admission: nobody knows yet whether AI will bring rapid growth, widespread unemployment, neither, or something else. It sets out different scenarios and asks how we'd tell which one is happening, which is useful if you're thinking about how your own job might change.

Source: [Anthropic ↗](https://www.anthropic.com/institute/econ-scenarios)

### A security researcher says one car brand's vehicles can be unlocked worldwide

A widely discussed write-up titled 'Unlocking any car from X brand in most of the world' describes a security flaw that a researcher says affects one car maker's vehicles in most countries. It's a reminder that connected cars depend on the same online systems as the apps on your phone, and those systems can have holes.

Source: [shubs.io ↗](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/)

### How one writer fights 'AI brain fry'

A popular blog post describes the mental fatigue of working with AI tools all day and the habits the author uses to stay sharp. If constant prompting and checking AI output leaves you drained, it offers practical ideas rather than a lecture.

Source: [Sergey Kuhne ↗](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

---
## Under the Hood

### Llama-modchip runs a 284-billion-parameter DeepSeek model on 64GB of RAM, no GPU

**What happened**
An open-source project called llama-modchip says it can run a 284-billion-parameter DeepSeek model on a machine with 64GB of ordinary memory and no graphics card. Models this size normally need expensive GPU hardware to run at all.

**Why it matters**
If approaches like this hold up, very large open models could run on high-end desktops instead of rented cloud GPUs, which matters for anyone who wants to keep data on their own machine. Check the repository for speed figures before planning around it, since running without a GPU usually means slower answers.

Source: [GitHub (synchopate/llama-modchip) ↗](https://github.com/synchopate/llama-modchip)

### GitHub has copied almost every repository to Azure on the way to 'agent-scale' Git

**What happened**
Previously covered on 2026-11-06: GitHub described a new Git storage design built so thousands of AI agents can push to one repository at once. Since then, GitHub says it has moved a copy of 99.99999% of its repositories to Azure, and explains how 'per-reference quorums' will bring over the rest while object storage lets reads scale separately from writes.

**Why it matters**
This is the plumbing behind a future where many AI agents work on the same codebase at the same time. For platform and infrastructure engineers, it's a detailed look at migrating one of the largest Git installations in the world.

Source: [GitHub Blog ↗](https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/)

---
**Fun fact:** GitHub says it has copied 99.99999% of its repositories to Azure, and only the last fraction is still to move.

*Daily tech digest for curious professionals. AI news that affects your work.*