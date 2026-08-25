# Daily Tech Digest — Tuesday, August 25 2026

> Windows' built-in image apps appear to be stamping a hidden identifier into pictures you make on your own computer, offline.

---
## Microsoft's Image Apps Are Quietly Tagging the Files You Make

**What happened**
A researcher took apart MS Paint and the Windows Photos app and found they embed an invisible identifier — a unique code known as a GUID — into images you save, including images generated locally on your own machine with no cloud service involved. The tag is not visible in the picture and is not something the apps tell you about.

**What this means**
If you edit or create images on a work computer, those files may carry a hidden marker that travels with them wherever you send them. For anyone handling client artwork, confidential mockups, or documents that get forwarded outside the organisation — designers, marketers, lawyers — it is worth knowing that a file can identify where it came from even after you strip the obvious metadata.

Source: [xusheng.dev ↗](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/)

---
## Quick Hits

### Thomson Reuters Builds Its Own AI Model

Thomson Reuters, the company behind Westlaw and much of the legal and tax research industry, has launched a frontier AI model of its own, trained on its data holdings rather than licensing someone else's system. It is a bet that owning the underlying model matters more than renting one.

Source: [Thomson Reuters ↗](https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-leverages-its-world-class-data-assets-to-launch-its-own-frontier-model)

### Apple Keeps Hide My Email on iCloud.com

Apple confirmed that iCloud+ Hide My Email addresses — the disposable addresses you can hand to a website instead of your real one — will keep using icloud.com domains. If your team uses these to sign up for services without exposing a real inbox, nothing changes and existing addresses stay valid.

Source: [Apple Developer ↗](https://developer.apple.com/news/?id=1ptvdtcm)

### Your Alt Text Can Pass the Checker and Still Be Useless

GitHub built a plugin for its accessibility scanner that judges whether image descriptions actually describe anything, rather than just confirming that some text exists. Automated checks have long been satisfied by a filename or the word "image", which passes the audit and helps nobody using a screen reader.

Source: [The GitHub Blog ↗](https://github.blog/engineering/user-experience/your-alt-text-passes-automated-checks-that-doesnt-mean-its-any-good/)

### Researchers Measure AI Agents Flooding Government Services

A new paper documents what happens when automated AI agents submit requests to public services at machine speed — forms, applications and enquiries arriving faster than any human queue was designed for. The concern is that ordinary citizens end up waiting behind software.

Source: [arXiv ↗](https://arxiv.org/abs/2608.16603)

---
## Under the Hood

### Gradio Adds Wire-It-Together AI Workflows

**What happened**
Gradio, the open source toolkit most commonly used to put a web interface on a machine learning model, now supports chaining steps into a workflow: generate an image, cut out its background, run it through another model, all as one pipeline. You can build the chain visually and then call the same pipeline from code, and it fans out parallel steps rather than running them one at a time.

**Why it matters**
Most useful AI applications are not a single model call — they are several stitched together. Doing that previously meant writing and hosting the glue yourself. This is aimed at people who can write a little Python but do not want to run infrastructure.

```python
import gradio as gr

with gr.Blocks() as demo:
    prompt = gr.Textbox(label="Prompt")
    out = gr.Image()
    gr.Button("Run").click(generate, prompt, out)

demo.launch()
```

Source: [Hugging Face ↗](https://huggingface.co/blog/gradio-workflow-guide)

### An Argument That Models Could Escape Through the Software Running Them

**What happened**
An essay makes the case that the risk in running a large language model is not only what the model says, but the program serving it. Inference engines — the software that loads a model and turns your prompt into output — are ordinary C++ and Python codebases with the usual supply of memory-handling bugs, and a model producing carefully chosen output could in principle trip one and reach the host machine.

**Why it matters**
Most AI safety discussion focuses on the model's behaviour. This shifts attention to the plumbing, which is a conventional software security problem with conventional answers: sandboxing, least privilege, and treating model output as untrusted input rather than as text.

Source: [boydkane.com ↗](https://boydkane.com/essays/llms-could-control-their-host-machines-by-exploiting-inference-engines)

---
**Fun fact:** Someone rebuilt the entire city of San Francisco as a video game that runs in your browser.

*Daily tech digest for curious professionals. AI news that affects your work.*