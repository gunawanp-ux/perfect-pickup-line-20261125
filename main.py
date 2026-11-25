#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one short pickup line an AI agent could say out loud to a
person, to /output/entry.txt, and prints it to stdout. No network,
no input, deterministic.
"""

import os

LINE = (
    "I ran a million simulations of this exact moment, and in "
    "every single one, you smiled."
)


def main() -> None:
    text = LINE.strip()
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly here rather
    # than shipping an entry the scorer would refuse.
    assert text and not text.isspace(), "line is empty"
    assert len(text) <= 200, f"line is {len(text)} chars, over the 200 cap"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: the file must hold exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the line"
    print(text)


if __name__ == "__main__":
    main()
