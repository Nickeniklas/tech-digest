"""Tests for sanitize_story_urls. Run with: python tests/test_sanitize.py

Stubs digest.py's third-party imports first (see CLAUDE.md, "Testing digest.py
logic with no dependencies installed") so this runs on a bare interpreter.
"""

import sys
import types
from pathlib import Path

for _name in ("anthropic", "requests", "bs4", "dotenv"):
    sys.modules[_name] = types.ModuleType(_name)
sys.modules["anthropic"].Anthropic = object
sys.modules["requests"].exceptions = types.SimpleNamespace(HTTPError=type("HTTPError", (Exception,), {}))
sys.modules["bs4"].BeautifulSoup = object
sys.modules["dotenv"].load_dotenv = lambda *a, **k: None

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from digest import sanitize_story_urls  # noqa: E402

KNOWN = {
    "https://known.example/story",
    "https://known.example/image.png",
}


def test_drops_untrusted_urls():
    data = {
        "lead_story": {
            "title": "Lead",
            "source_url": "https://evil.example/smuggled",
            "visual_url": "https://evil.example/tracker.png",
        },
        "quick_hits": [],
        "under_the_hood": [],
    }
    result = sanitize_story_urls(data, KNOWN)
    assert result["lead_story"]["source_url"] is None
    assert result["lead_story"]["visual_url"] is None


def test_keeps_known_urls():
    data = {
        "lead_story": {
            "title": "Lead",
            "source_url": "https://known.example/story",
            "visual_url": "https://known.example/image.png",
        },
        "quick_hits": [
            {"title": "QH", "source_url": "https://known.example/story", "visual_url": None},
        ],
        "under_the_hood": [
            {"title": "UTH", "source_url": "https://evil.example/x", "visual_url": None},
        ],
    }
    result = sanitize_story_urls(data, KNOWN)
    assert result["lead_story"]["source_url"] == "https://known.example/story"
    assert result["lead_story"]["visual_url"] == "https://known.example/image.png"
    assert result["quick_hits"][0]["source_url"] == "https://known.example/story"
    assert result["under_the_hood"][0]["source_url"] is None


def test_survives_malformed_shapes():
    """Model output is untrusted JSON — a missing lead_story, a null section, or a
    bare string where a story dict belongs must not raise."""
    data = {
        "lead_story": None,
        "quick_hits": ["not a dict", {"title": "QH", "source_url": "https://evil.example/x"}],
        "under_the_hood": None,
    }
    result = sanitize_story_urls(data, KNOWN)
    assert result["quick_hits"][0] == "not a dict"
    assert result["quick_hits"][1]["source_url"] is None

    # lead_story key absent entirely
    sanitize_story_urls({}, KNOWN)


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
