#!/usr/bin/env python3
"""Make the AI Judge Laugh entry: writes one original office-life joke to /output/entry.txt.

The joke is built from three fragments: a SETUP (the ask — a raise), a
TWIST (what the boss gave instead — a new title), and a PUNCH (the sting
in the last words — same pay, longer signature). Title inflation in place
of money is a true office observation; the laugh lands on "longer
signature", the one thing the new title actually changed.
"""

import os

MAX_CHARS = 200

# Setup: the ask — a raise, the honest office request.
SETUP = "I asked for a raise"
# Twist: what the boss gave instead — a new title, not money.
TWIST = "and got a new title instead"
# Punch: the sting — the title changed nothing but the signature.
PUNCH = "\u2014 same pay, longer signature."


def assemble():
    """Join the fragments into the single joke line."""
    return f"{SETUP} {TWIST} {PUNCH}"


def validate(text):
    """Gate: 1-200 characters of UTF-8 text, not only whitespace, one line.

    Also enforces the brief's one-breath rule: a single line of at most
    25 words, so the joke reads aloud in one breath.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if len(words) > 25:
        raise ValueError(f"entry must read in one breath (<=25 words), got {len(words)}")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
