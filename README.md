# tech-digest

Daily tech news digest for developers. Fetches the latest AI and dev tools news from high-signal sources, summarizes it with Claude, and emails a styled HTML newsletter to your inbox every morning.

## What it does

1. Searches HackerNews, GitHub Trending, HuggingFace, and official changelogs for today's most relevant developer news
2. Selects the 3–5 most actionable stories and writes them up with an editorial voice
3. Generates a polished HTML email and a Markdown file
4. Sends the email via Gmail and saves both files locally

## Requirements

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com) (uses `claude-sonnet-4-6`)
- A Gmail account with [App Password](https://myaccount.google.com/apppasswords) enabled (requires 2FA)

## Setup

```bash
git clone https://github.com/yourusername/tech-digest
cd tech-digest

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=sk-ant-...
GMAIL_APP_PASSWORD=your16charpassword
MAIL_FROM=you@gmail.com
MAIL_TO=you@gmail.com
```

## Usage

```bash
python digest.py
```

Output files are saved to `digests/`:

```
digests/
├── tech-digest-2026-04-02.md
├── tech-digest-2026-04-02.html
└── raw_response.txt        # Claude's raw output, useful for debugging
```

## Scheduling (Windows)

To run automatically every morning, set up a Windows Task Scheduler task:

1. Open Task Scheduler → Create Basic Task
2. Set trigger: Daily at your preferred time (e.g. 07:00)
3. Action: Start a program
   - Program: `C:\Users\<you>\projects\tech-digest\venv\Scripts\python.exe`
   - Arguments: `digest.py`
   - Start in: `C:\Users\<you>\projects\tech-digest`

## Cost

Roughly **$0.10–0.15 per run** using `claude-sonnet-4-6` + web search. At daily usage that's ~$3–4/month.

## Project structure

```
tech-digest/
├── digest.py          # Main script
├── CLAUDE.md          # Claude Code instructions
├── requirements.txt
├── .env               # API keys (never commit this)
├── .gitignore
└── digests/           # Generated output files
```