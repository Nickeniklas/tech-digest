"""End-to-end tests for finish_stage with malformed model output.
Run with: python tests/test_finish_stage.py  (needs jinja2, e.g. the repo venv)

Stubs digest.py's other third-party imports first (see CLAUDE.md, "Testing
digest.py logic with no dependencies installed"). finish_stage writes files
relative to the working directory, so each test runs in a temp dir with
SEEN_TOPICS_PATH pointed there too — the repo's digests/, index.html,
archive.html and seen_topics.json are never touched.
"""

import json
import os
import sys
import tempfile
import types
from pathlib import Path

for _name in ("anthropic", "requests", "bs4", "dotenv"):
    sys.modules[_name] = types.ModuleType(_name)
sys.modules["anthropic"].Anthropic = object
sys.modules["requests"].exceptions = types.SimpleNamespace(HTTPError=type("HTTPError", (Exception,), {}))
sys.modules["bs4"].BeautifulSoup = object
sys.modules["dotenv"].load_dotenv = lambda *a, **k: None

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import digest  # noqa: E402

KNOWN = {"https://known.example/story"}
LEAD_MARKUP = 'class="lead-kicker">Lead Story<'


def _raw(data: dict) -> str:
    return f"<!-- BEGIN_JSON -->{json.dumps(data)}<!-- END_JSON -->"


def _run_finish(data: dict) -> tuple[str, str]:
    """Run finish_stage in a temp dir; return (markdown, html) it wrote."""
    old_cwd, old_seen = os.getcwd(), digest.SEEN_TOPICS_PATH
    with tempfile.TemporaryDirectory() as tmp:
        try:
            os.chdir(tmp)
            digest.SEEN_TOPICS_PATH = Path(tmp) / "seen_topics.json"
            md_path, html_path = digest.finish_stage("2026-01-01", "January 1, 2026", _raw(data), KNOWN)
            return md_path.read_text(encoding="utf-8"), html_path.read_text(encoding="utf-8")
        finally:
            os.chdir(old_cwd)
            digest.SEEN_TOPICS_PATH = old_seen


def test_null_lead_story_does_not_crash():
    md, html = _run_finish({
        "teaser": "Teaser",
        "lead_story": None,
        "quick_hits": [{"title": "QH", "summary": "S.", "source_name": "Src",
                        "source_url": "https://known.example/story"}],
        "under_the_hood": None,
    })
    assert LEAD_MARKUP not in html
    assert "## Quick Hits" in md and "### QH" in md


def test_malformed_sections_and_teaser():
    md, html = _run_finish({
        "lead_story": "not a dict",
        "quick_hits": ["bare string", {"title": "QH"}],
        "under_the_hood": "also not a list",
    })
    assert "### QH" in md
    assert "Under the Hood" not in md
    assert LEAD_MARKUP not in html


def test_valid_lead_story_still_renders():
    md, html = _run_finish({
        "teaser": "Teaser",
        "lead_story": {"title": "Lead", "what_happened": "W.", "what_this_means": "M.",
                       "source_name": "Src", "source_url": "https://known.example/story"},
        "quick_hits": [],
        "under_the_hood": [],
    })
    assert "## Lead" in md
    assert LEAD_MARKUP in html and "Lead</h2>" in html


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {test.__name__}: {e or 'assertion failed'}")
        except Exception as e:
            failed += 1
            print(f"ERROR {test.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
