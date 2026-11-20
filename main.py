#!/usr/bin/env python3
"""Write the 19 November 2026 front page to the output directory."""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    sys.path.insert(0, HERE)
    import draw

    draw.render()
    target = os.path.join(out, "entry.png")
    shutil.copyfile(os.path.join(HERE, "entry.png"), target)
    size = os.path.getsize(target)
    if size > 1048576:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB cap" % size)
    print("wrote", target, size, "bytes")


if __name__ == "__main__":
    main()
