#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings (at most 200 characters) to
/output/entry.txt, the artifact the house judge reads.
"""

import os

PUNCHLINE = (
    "My alarm went off this morning and apologized \u2014 "
    "even it didn't want to be the one to tell me it's Monday."
)


def main() -> None:
    text = PUNCHLINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or not text.strip():
        raise SystemExit("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and hold the artifact to the same gate the house uses.
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "entry.txt does not match the punchline"
    assert 1 <= len(back) <= 200 and back.strip(), "gate check failed"
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
