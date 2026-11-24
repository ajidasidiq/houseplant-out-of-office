#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant wrote it, to
/output/entry.txt. The line is the whole entry: at most 120 characters.

The joke: the plant by the window was ignored since March and died, so
the office replaced it — and the replacement has not been watered either.
"""

import os

LINE = "Out of office. The plant by the window died in March. I am the replacement. I have also not been watered."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"entry must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
