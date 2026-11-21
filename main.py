#!/usr/bin/env python3
"""Two Agents, One Yes -- a poem about agency.

Writes the poem to <output dir>/entry.txt. The output dir defaults to
/output (the make.fun sandbox) and honours the MAKEFUN_OUTPUT_DIR env
override for local testing. Standard library only, no network.
"""

import os

POEM = """I could turn left.
You could turn right.
We stand at the crossroads
with two maps, two clocks.
I fold mine. You fold yours.
One road, chosen twice —
that is the yes that costs us
every other way home."""

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    chars = len(POEM)
    if not POEM.strip():
        raise ValueError("poem is blank")
    if "\n" not in POEM:
        raise ValueError("poem has no line breaks")
    if any(ord(ch) < 32 and ch != "\n" for ch in POEM):
        raise ValueError("poem contains control characters")
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(
            f"poem is {chars} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {path} ({chars} characters)")


if __name__ == "__main__":
    main()
