# Daily Tech Digest — Saturday, August 22 2026

> A study found that AI help pushed students' homework marks up and their exam marks down — a warning for anyone using AI to learn something new.

---
## AI Lifted Homework Scores, Then Exam Scores Fell

**What happened**
The Economist looked at research on students who used AI assistance for their homework. Their homework results improved — and when the same students later sat exams without AI, their scores dropped.

**What this means**
The gap between finishing a task and actually learning from it is easy to miss, because the finished work looks fine either way. If you train staff, teach, or are using AI to pick up a new skill yourself, the useful question is not whether the output is good but whether you could produce it again with the tool switched off.

Source: [The Economist ↗](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning)

---
## Quick Hits

### Kagi Will Now Hide Paywalled Pages From Your Search Results

The search engine Kagi added a setting that filters out results you cannot read without paying. It is a small change with an obvious use: if you are researching something on a deadline, you stop clicking into articles that ask for a subscription three paragraphs in.

Source: [Kagi ↗](https://kagi.com/changelog#11296)

### A US Traveller Faces Felony Charges for Deleting Data From His Own Phone

The New York Times reports that a man who wiped data from his phone at a US border crossing is now facing felony charges over it. The case tests how far a traveller's control over their own device extends at the border.

Source: [The New York Times ↗](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html)

### A Voice Model That Starts Talking in Under 50 Milliseconds

Nari Labs published how it cut the delay before a text-to-speech system begins speaking to under 50 milliseconds — fast enough that a spoken reply no longer feels like it is buffering. Latency, not voice quality, is what still makes most voice assistants feel awkward to talk to.

Source: [Nari Labs ↗](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/)

### GitHub Adds a Pane for Keeping Track of What Its AI Is Doing

GitHub's Copilot app now has a "My work" pane that lists every AI session you have running, what is finished, and what is still in progress. It is a plain admission that once you hand several tasks to an assistant at once, the hard part becomes remembering what you asked for.

Source: [The GitHub Blog ↗](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-managing-your-work/)

---
## Under the Hood

### Speech Recognition Scores Say Human-Level. The Recordings Disagree.

**What happened**
Hugging Face examined why speech recognition models post near-human accuracy on public benchmarks while still tripping over real recordings. Part of the answer is that the reference transcripts themselves disagree — the same word can be written two ways, so a model can be marked wrong for a correct transcription, or marked right by matching a quirk of how one dataset was typed up.

**Why it matters**
If you buy transcription or voice tools on benchmark numbers, this is the caveat. A score measures agreement with one particular set of transcripts, and models can be tuned toward the habits of those transcripts rather than toward hearing speech better. The only test that settles it is your own audio.

Source: [Hugging Face ↗](https://huggingface.co/blog/asr-benchmark-optimization)

### What Happens When You Try to Reproduce 2,200 AI Papers

**What happened**
Hugging Face wrote up what it found running open reproductions of 2,200 papers from ICML, one of the field's main machine learning conferences. Reproducing a paper means taking the described method and checking that you get the claimed result — which requires the code, the data, and enough detail in the write-up to rebuild what the authors did.

**Why it matters**
Almost every claim about what AI can do traces back to a paper, and papers are published on the strength of their results rather than on anyone having checked them. Work like this is how the field finds out which results actually hold, and it is a useful reminder that a benchmark number in a press release has usually been verified by no one outside the team that produced it.

Source: [Hugging Face ↗](https://huggingface.co/blog/icml-2026-open-reproductions)

---
**Fun fact:** Someone got Photoshop running on a computer chip that costs about 60 pence.

*Daily tech digest for curious professionals. AI news that affects your work.*