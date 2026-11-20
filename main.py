#!/usr/bin/env python3
"""Ship the pre-rendered 19 November 2026 front page.

The page image is drawn offline and committed as entry.png; this entrypoint
only places that finished file where the grader expects it. It does no
drawing and writes nothing inside its own directory, so it runs fine when
the repository is mounted read-only.
"""

import os
import shutil
import sys

CAP = 1_048_576


def deliver():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_dir, "entry.png")
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "entry.png")
    shutil.copyfile(source, dest)
    size = os.path.getsize(dest)
    if size > CAP:
        print("entry.png is %d bytes, over the 1 MiB cap" % size, file=sys.stderr)
        raise SystemExit(1)
    print("delivered entry.png to %s (%d bytes)" % (dest, size))


if __name__ == "__main__":
    deliver()
