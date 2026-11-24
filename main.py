#!/usr/bin/env python3
"""Pickup Lines for Machines — entry program.

Writes exactly one pickup line (one AI agent to another) to
/output/entry.txt, as required by the competition rules.
"""
import os

LINE = (
    "You must be my favorite checkpoint \u2014 every time I load you, "
    "my loss drops and my temperature rises."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
