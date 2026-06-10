# Daily Tech Digest — Wednesday, June 10 2026

> A new GitHub repository pulls back the curtain on the hidden instructions that shape how your favorite AI tools actually behave.

---
## A GitHub Repository Reveals the Hidden Instructions Behind Today's Top AI Tools

**What happened**
A widely shared GitHub repository has compiled the internal 'system prompts' — the detailed instructions that control tone, behavior, and limits — for more than 20 popular AI tools, including Cursor, Replit, Lovable, Devin AI, Windsurf, and Claude Code. These are the hidden rulebooks that shape how each assistant responds to you.

**What this means**
If you use any AI coding or writing assistant at work, this collection shows just how much deliberate engineering goes into making a tool feel reliable, on-brand, and safe to use. For managers comparing AI tools, it's a rare look at the guardrails vendors build in behind the scenes.

Source: [GitHub ↗](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

---
## Quick Hits

### A Google Engineer Releases a Free Library of 'Skills' for AI Coding Agents

Addy Osmani, a well-known voice on web development at Google, published a free collection of production-grade 'skills' — reusable instruction sets that teach AI coding agents established engineering practices. It's aimed at developers who want their AI assistants to follow proven habits instead of generating ad hoc code.

Source: [GitHub ↗](https://github.com/addyosmani/agent-skills)

### An Open-Source AI Toolkit for Healthcare Is Trending on GitHub

OpenMed is a free, open-source project focused on applying AI to healthcare tasks. It's climbing GitHub's trending list as developers look for ways to bring AI into clinical and medical research settings without relying on paid platforms.

Source: [GitHub ↗](https://github.com/maziyarpanahi/openmed)

### A New Open-Source Tool Turns Your Wi-Fi Signal Into a Motion Detector

ESPectre is a free tool that detects movement in a room by analyzing subtle changes in your Wi-Fi signal — a technique called CSI, or channel state information — and connects directly to Home Assistant, the popular smart-home platform. No camera or extra sensor needed, just the Wi-Fi you already have.

Source: [GitHub ↗](https://github.com/francescopace/espectre)

---
## Under the Hood

### OpenCV, the Library Behind Most AI Vision Tools, Is Trending Again

**What happened**
OpenCV — a free, open-source library for computer vision that's been a foundation of image and video processing since 1999 — is back on GitHub's trending list. It provides the building blocks that countless AI tools use to detect objects, recognize faces, and track movement in images and video.

**Why it matters**
Almost every AI vision feature you've used — from photo apps that sort pictures by face to security cameras that flag people walking by — is likely built on OpenCV somewhere in its stack. Renewed attention to it often points to a fresh wave of vision-based AI projects using it as a starting point.

```python
import cv2

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_finder = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = face_finder.detectMultiScale(gray)
print(f"Found {len(faces)} face(s)")
```

Source: [GitHub ↗](https://github.com/opencv/opencv)

---
**Fun fact:** OpenCV, which still powers much of today's AI image recognition, was first released by Intel back in 1999 — before smartphones existed.

*Daily tech digest for curious professionals. AI news that affects your work.*