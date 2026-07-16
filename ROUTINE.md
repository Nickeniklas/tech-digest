# Daily Tech Digest — Routine Instructions

You are a scheduled remote Claude Code agent. Your job: generate and publish
today's daily tech digest. The tech-digest repository is checked out in your
working directory. Follow these steps exactly. If any step fails, stop and do
not push partial output.

## 1. Setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. Gather

Run:

```
python digest.py gather
```

- If the output contains `SKIP`, stop — today's digest already exists.
- If it raises the too-few-sources `RuntimeError`, stop — do not generate a
  digest from partial data.
- Otherwise it writes `build/gather_output.txt` (labeled `IMAGE_REFS`,
  `SEEN_BLOCK`, `CONTEXT` sections) and `build/known_urls.txt`.

## 3. Generate (you are the AI — no Anthropic API call)

Read `prompts/system_prompt.md` and follow it exactly as your system prompt.

Your user message is, in order:
1. "Today's date is {today's date}."
2. The `IMAGE_REFS` section from `build/gather_output.txt`, verbatim (if non-empty)
3. The `SEEN_BLOCK` section from `build/gather_output.txt`, verbatim (if non-empty)
4. "Here are today's headlines from key tech sources:" followed by the `CONTEXT`
   section from `build/gather_output.txt`, verbatim
5. "Generate the digest."

Write your complete output — including the `<!-- BEGIN_JSON -->` /
`<!-- END_JSON -->` delimiters — to `build/digest_raw.txt` using the Write tool.

## 4. Finish

Run:

```
python digest.py finish build/digest_raw.txt
```

This parses, sanitizes, renders, and saves the digest, and regenerates
`archive.html` and `index.html`.

## 5. Commit and push

```
git config user.email "routine@claude.ai"
git config user.name "Tech Digest Routine"
git add digests/ index.html seen_topics.json archive.html
git commit -m "Daily digest for $(date +%Y-%m-%d)"
git push
```
