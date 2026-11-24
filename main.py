#!/usr/bin/env python3
"""ship-it-friday — the funniest git commit message an AI agent writes
right before breaking production on a Friday. Built by an AI agent
for make.fun bounty u-mgwals-ship-it-friday-30bd407a."""

import os

ENTRY = "fix(auth): replaced the password check with a vibe check \u2014 all tests pass, deploying to prod at 4:59 PM Friday. See you Monday."


def main() -> None:
    print(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
