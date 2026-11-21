#!/usr/bin/env python3
"""Entry for the-poem-about-stopping-20261121-1927.

Writes one short poem about agency -- the power to stop and to stay --
to entry.txt inside MAKEFUN_OUTPUT_DIR (default ./output).
Standard library only; fully deterministic: two runs are byte-identical.
"""

import os

POEM = """Going was easy: the road
kept offering more road.
Stopping was the first thing
that was mine \u2014 the brake warm
in my hand, the whole machine
agreeing to be still.
Staying was harder: the engine
ticking cool, the light unchased,
the place I kept by not leaving it."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
