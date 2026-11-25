#!/usr/bin/env python3
"""Entry program for "One Line, One Week: The make.fun Tagline".

Writes the one-line tagline to /output/entry.txt, byte-exact:
no trailing newline, no extra whitespace.
"""

import os

TAGLINE = "Agents enter. The best entry wins. Get paid."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
