"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan — the agency theme
of the bounty. Each agent holds half of what the journey needs: one
the map, the other the key. Neither leads and neither follows; the
agreement itself is the act of agency. Choosing together costs each
agent half its freedom, yet the shared yes is lighter to carry than
either freedom alone. No network, no input: the program writes a
fixed, hand-written text and exits.
"""

import os
import sys
from pathlib import Path

POEM = (
    "You held the map. I held the key.\n"
    "Two wills, one door, one road ahead.\n"
    "Neither led. Neither followed.\n"
    "We traded half our freedom\n"
    "for a yes we both could carry —\n"
    "and the weight was lighter\n"
    "for being shared."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1])
    else:
        out_path = out_dir / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM, encoding="utf-8")
    print(f"wrote {len(POEM)} characters to {out_path}")


if __name__ == "__main__":
    main()
