#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters,
in the voice of a robot trying to charm someone, to /output/entry.txt.
"""

import os

LINE = "Are you a CAPTCHA? My processors have verified you three times and still can't believe you're real."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
