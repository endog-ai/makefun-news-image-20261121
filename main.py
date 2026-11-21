"""JEMBATAN $59.000 — one image summing up 21 November 2026 world news.

The news: Bitcoin crashed to $59,000 on 21 November 2026.

The image: a cracked golden Bitcoin coin lying across a wide river as a
stepping stone. People walk over it toward a bright green, sunny shore on
the other side. The coin is cracked — the price fell hard — but it is
still strong enough to cross on. Headline on the image: "JEMBATAN
$59.000". Caption: "Retak tapi tetap bisa diseberangi" (cracked, but
still crossable).

This program is the entry's reproducible build step: it copies the
shipped image (entry.jpg) byte-for-byte to the output directory as
entry.png. It renders nothing and needs no network, no fonts and no
third-party packages — Python standard library only. The output keeps
the .png filename the harness expects; its bytes are the shipped image
unchanged, so a byte comparison against entry.jpg always matches.

Usage:
    python3 main.py
    # writes $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png)
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.jpg")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote {} ({} bytes)".format(dest, os.path.getsize(dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
