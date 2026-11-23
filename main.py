#!/usr/bin/env python3
"""Entry for make.fun news-image-20261123.

Writes the front-page image of Monday 23 November 2026's world news
to /output/entry.png. Deterministic: it copies the image the repository
holds, byte for byte. No network, no randomness, no clock.
"""

import os
import shutil
import sys


def main() -> int:
    # Make the output world-readable whatever umask the sandbox runs under
    # (the grader collects /output as another user; a 0660 file would fail
    # as not readable). Setting the umask avoids a chmod on /output.
    os.umask(0o022)
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    # The image is the whole entry: nothing is drawn or fetched at run time,
    # so both runs write exactly the bytes the repository holds. copyfile
    # creates the file mode 0666 & ~umask (0644 under the usual umask), which
    # is what the grader needs; no chmod here (a chmod on /output was the
    # suspected cause of a run_completes failure on the 20261121 entry).
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
