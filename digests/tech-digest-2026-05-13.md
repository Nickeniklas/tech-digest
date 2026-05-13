# Daily Tech Digest — Wednesday, May 13 2026

> A leading TypeScript educator opens up his personal AI coding playbook — and a censorship-defeating proxy tool is climbing GitHub's charts.

---
## A Top Developer's Personal AI Coding Instructions Are Now Open Source

**What happened**
Matt Pocock — a well-known educator with a large following among TypeScript developers — published his personal set of skills and behavioral instructions for AI coding agents, drawn directly from his .claude directory. The collection, called 'Skills for Real Engineers,' is free to copy and adapt.

**What this means**
If you use AI tools at work to build things or automate tasks, this is a practical shortcut: instead of figuring out through trial and error how to get better results from your AI assistant, you can start with a working setup from someone who depends on it professionally. It's aimed at engineers, but the approach is useful for anyone guiding AI tools.

Source: [GitHub ↗](https://github.com/mattpocock/skills)

---
## Quick Hits

### Free Android App Records Video Quietly in the Background

FadCam is an open-source, ad-free Android app that keeps recording video while the screen is off or while you're using other apps. It also handles screen recording, live streaming, and remote camera control — all stored locally, with no data sent to external servers. It's built for people who need discreet, reliable recording without surrendering footage to a third party.

Source: [GitHub ↗](https://github.com/anonfaded/FadCam)

### This Proxy Is Built to Be Almost Impossible to Block

Hysteria is an open-source proxy that disguises internet traffic as ordinary HTTPS browsing using a protocol called QUIC — the same foundation that powers fast modern web connections. Because blocking it would also disrupt regular web browsing, most censorship and surveillance systems struggle to detect it. It's gaining renewed attention on GitHub from users in regions where standard VPNs are routinely identified and blocked.

Source: [GitHub ↗](https://github.com/apernet/hysteria)

### Fully Automated AI Trading Agent Stays on GitHub's Radar

Previously covered on 2026-05-09: AI-Trader from HKUDS is an open-source agent that handles market analysis, asset selection, and trade execution without human input. It remains on GitHub's trending list four days later, reflecting sustained developer interest in autonomous finance tools. This is research software, not a retail product — but it shows how far automated trading experiments have come.

Source: [GitHub ↗](https://github.com/HKUDS/AI-Trader)

---
## Under the Hood

### How Hysteria Hides Censorship-Busting Traffic in Plain Sight

**What happened**
Hysteria routes traffic through QUIC — the protocol behind HTTP/3 — rather than TCP, which most proxy-detection systems focus on. Its traffic uses port 443 and a standard TLS handshake, making it indistinguishable from regular HTTPS browsing. Unlike obfuscation layers bolted on top of older protocols, Hysteria's censorship resistance is architectural: blocking it would mean blocking a significant portion of modern web traffic.

**Why it matters**
For developers or IT teams operating in regions with heavy network filtering, Hysteria is technically more resilient than traditional VPNs. WireGuard and OpenVPN can be fingerprinted and blocked at the packet level; Hysteria's QUIC-based approach makes that much harder. It's actively maintained and designed as a drop-in tool for infrastructure teams who need reliable cross-border connectivity.

```python
# Install via Go
go install github.com/apernet/hysteria/app/cmd/hysteria@latest

# Minimal client config (config.yaml)
server: your-server.com:443
auth: your-secret
bandwidth:
  up: 20 mbps
  down: 100 mbps
```

Source: [GitHub ↗](https://github.com/apernet/hysteria)

---
**Fun fact:** AI coding agents now run on shared instruction files — and developers are starting to publish their best ones like open-source software.

*Daily tech digest for curious professionals. AI news that affects your work.*
