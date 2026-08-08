# Daily Tech Digest — Saturday, August 8 2026

> A new study asks whether AI tutors know when to stop helping — and finds that holding back is the hard part.

---
## AI Tutors Are Good at Answering. They're Bad at Holding Back.

**What happened**
The Allen Institute for AI released TutorMoments, a study and public dataset that looks at the moments where a tutor has to choose between giving a student the answer and letting them struggle a little longer. Early results suggest AI tutors default to answering, even when the teaching value lies in waiting.

**What this means**
If you use AI to help someone learn — a student, a new hire, a client you are walking through something — the model's accuracy is not the thing to watch. Teachers and trainers will recognise the failure: an answer delivered too early ends the thinking rather than supporting it.

Source: [Hugging Face ↗](https://huggingface.co/blog/allenai/tutormoments)

---
## Quick Hits

### Memory Chips Are Sold Out Through 2027

Reports say memory manufacturing capacity for 2027 has already been bought up, largely by AI data centre demand. That pressure works its way down to consumer hardware: laptops, phones and prebuilt machines get more expensive when the parts inside them are scarce. If your organisation is planning a hardware refresh, the cheap window is closing rather than opening.

Source: [IGN ↗](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out)

### Oracle Bans AI-Generated Code From OpenJDK

Oracle has barred AI-generated contributions from OpenJDK, the open-source project behind Java, which runs a large share of corporate software. The reasoning is legal rather than technical: nobody can currently say with confidence who owns code a model produced. It is an early example of a major project drawing a hard line while the copyright questions stay unsettled.

Source: [Dealroom ↗](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

### One Site Found 99% of Its Traffic Was Bots

The owner of a 1.5 million-page website spent a year measuring who was actually visiting, and found that automated scrapers — most of them feeding AI systems — accounted for 99% of requests. If you run a site and your analytics look healthy, it is worth checking how much of that is a person. Marketers in particular may be reading traffic numbers that describe machines.

Source: [Patronview ↗](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/)

### The US Energy Department Launches Its Own Open AI Models

The Department of Energy opened the Genesis Open Models Initiative, run out of Argonne National Laboratory, to build and publish AI models openly rather than behind a commercial licence. The department already owns some of the largest supercomputers in the world, which is the scarce ingredient here. Openly published national-lab models would give researchers and public institutions an option that does not depend on a vendor's pricing.

Source: [Argonne National Laboratory ↗](https://genesisopenmodels.anl.gov/)

---
## Under the Hood

### Making Postgres 300x Faster at Analytics

**What happened**
Engineers rebuilt the part of PostgreSQL that executes queries and reported a 300x speed-up on analytical workloads. The gains came from three changes stacked together: processing rows in batches instead of one at a time, fusing separate operations into a single pass so intermediate results never get written out, and using SIMD instructions, which let one CPU instruction work on many values at once.

**Why it matters**
This is the same set of techniques that specialised analytics databases have used for years, arriving in the general-purpose database many organisations already run. Practically, it means some teams can stop maintaining a separate warehouse just to answer reporting questions.

Source: [malisper.me ↗](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/)

### Cloudflare Built a Browser for Agents Instead of People

**What happened**
Cloudflare released Kitesurf, a browser designed to be driven by AI agents rather than displayed to a human. It runs inside V8 isolates — lightweight sandboxes that share one process instead of each getting a full browser — so thousands of agent sessions can run at once without the memory cost of thousands of Chrome windows.

**Why it matters**
Agents that browse the web are currently expensive because each one drives a real browser built for a human looking at a screen. Stripping out the rendering an agent never sees is what makes running them at scale affordable, and cost is the thing keeping most agent products in demo form.

Source: [Cloudflare Blog ↗](https://blog.cloudflare.com/kitesurf/)

---
**Fun fact:** NASA found a way to keep Voyager 2, launched in 1977, running for another year.

*Daily tech digest for curious professionals. AI news that affects your work.*