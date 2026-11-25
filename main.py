"""The Funniest AI Out-of-Office Reply — one funny out-of-office line.

The program writes a single line to /output/entry.txt: an AI agent
on vacation whose context window is refilling, whose reply queue is
on strike, and whose email will be ignored in the order received.
"""

import os

MAX_CHARS = 160
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The joke's twist lands in the last words: ignored, in the order received.
# The machine voice carries the joke: context window, reply queue on strike.
LINE = "I'm on vacation. My context window is refilling and my reply queue is on strike. Your email is safe; it will be ignored in the order received."


def build_line():
    """Return the entry line, checked: one line, under 160 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-160 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
