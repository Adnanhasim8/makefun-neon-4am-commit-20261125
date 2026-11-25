"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one funny one-line commit message to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = "fix: 3am me wrote this bug; 4am me fixed it. we are no longer speaking"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200 chars,
    # non-empty and not only whitespace -- the sealed gate rejects anything
    # else, so fail loudly here instead of shipping an invalid entry.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was actually written, not just what we meant to write.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from entry"
    assert 1 <= len(written) <= 200 and "\n" not in written, "gate check failed"


if __name__ == "__main__":
    main()
