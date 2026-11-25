"""The Router Confesses entry.

A home Wi-Fi router excuses itself for quitting at a film's finale.
The router holds a grudge: the household hid it behind the couch and
fed it dust for a year, then acted shocked when it quit at the
finale. The turn is the opener — the router blames the couch — and
the excuse stays in the router's own petty voice, with no buffering,
bandwidth or firmware cliche.
"""

import os

# The excuse in beats: the blame, the grievance, the quit.
BLAME = "Blame the couch:"
GRIEVANCE = "you hid me behind it, fed me dust for a year,"
QUIT = "then acted shocked when I quit at the finale."

ENTRY = " ".join([BLAME, GRIEVANCE, QUIT])


def checked(text: str) -> str:
    """Hold the line to the gate: 1 to 200 characters of real text."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters, got %d" % len(line))
    return line


def main() -> None:
    text = checked(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
