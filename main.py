#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one brutally honest but still polite out-of-office auto-reply
to /output/entry.txt: a single sentence, 154 characters.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I'm out of the office until Monday, and the honest version is that "
    "I am on holiday because work had me running on empty, and I'll reply "
    "once I'm refilled."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the one sentence, no trailing newline: 154 UTF-8 chars.
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
