#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Reads the roast line from roast.txt (strict UTF-8), validates it against
the competition gate (1-200 characters, not only whitespace, one line),
and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only; deterministic.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "roast.txt")


def load_line() -> str:
    with open(SOURCE, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")  # strict: raises on invalid UTF-8
    if text.endswith("\n"):
        text = text[:-1]
    return text


def validate(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    text = load_line()
    validate(text)
    data = text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Atomic write: temp file in the same directory, then rename over the
    # target, so a grader never sees a half-written entry.
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as fh:
        fh.write(data)
    os.replace(tmp_path, out_path)
    # Round-trip verification: the bytes on disk must match the line exactly.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise IOError("round-trip verification failed: entry.txt differs from roast.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
