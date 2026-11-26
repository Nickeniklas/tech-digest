# Daily Tech Digest — Thursday, November 26 2026

> Anthropic has upgraded its two most capable Claude models, aimed at the hardest work in coding, finance and science.

---
## Anthropic releases Claude Fable 5.2 and Claude Mythos 5.2

**What happened**
Anthropic has upgraded Claude Fable and Claude Mythos, the models it designs for the most demanding technical challenges. The company says the 5.2 versions set a new bar in coding, finance, and the sciences.

**What this means**
If you use Claude for complex analysis — financial modelling, research summaries, or large software projects — these are the versions to try for your hardest tasks. As always, check results on your own work before relying on the claims.

Source: [Anthropic ↗](https://www.anthropic.com/claude-fable-and-mythos-5-2)

---
## Quick Hits

### OpenAI tightens GPT-6.2 usage limits

OpenAI has cut how much you can use its GPT-6.2 models: according to a post shared on Hacker News, the Astra model now hits its limits 40% faster and Sol 25% faster. If your team relies on these models daily, expect to run into caps sooner.

Source: [Hacker News ↗](https://twitter.com/thsottiaux/status/2125784147889393806)

### The New York Times warns photographers not to update Photoshop

The Verge reports that The New York Times has told its photographers not to update Photoshop because of new AI features. For anyone whose images need to stay untouched and trustworthy — journalists, legal teams, archivists — it's a reminder to check what a software update changes before installing it.

Source: [The Verge ↗](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

### 1Password reports a security incident

1Password, the password manager used by many companies and individuals, has published an update on a security incident from November 2026. If you use it, read the company's post and follow any steps it recommends.

Source: [1Password ↗](https://1password.com/blog/update-on-nov-2026-security-incident)

### Where scientists draw the line on AI agents

AllenAI looks at how researchers decide what to hand off to AI. Delegating a task doesn't remove your responsibility: if AI reviews the literature for you, you still need to check it didn't miss conflicting evidence or overstate what papers say — a lesson that applies to any professional using AI for research.

Source: [HuggingFace Blog ↗](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents)

---
## Under the Hood

### Turning AI bug reports into fixes maintainers can use

**What happened**
In the Codename MDASH pilot, GitHub and Microsoft took thousands of raw AI-generated security findings and filtered them into 99 checked, private reports with suggested fixes, sent to six widely used open-source projects. Maintainers have already fixed more than half.

**Why it matters**
Open-source maintainers are flooded with low-quality AI bug reports. This pilot shows a better model: verify findings first, report privately, and attach a fix — less noise, more actual repairs.

Source: [GitHub Blog ↗](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/)

### Nfs2root: a 12-year-old remote root flaw in Linux's NFS server

**What happened**
Researchers disclosed CVE-2026-99362, a bug in the Linux kernel's NFS server — the part that shares folders over a network. It can give an attacker full control (root) without logging in first, and it has been in the code for about 12 years.

**Why it matters**
Any Linux machine exporting NFS shares is a potential target, so administrators should apply kernel updates as soon as their distribution ships them. A separate report today also criticises slow Ubuntu security response times.

Source: [opensec.in ↗](https://opensec.in/blog/nfs2root-cve-2026-99362)

---
**Fun fact:** Roald Dahl wrote a story about a machine that mass-produces novels — in 1954.

*Daily tech digest for curious professionals. AI news that affects your work.*