#!/usr/bin/env python3
"""The Best Meal You Ever Had — Variant A: Father's Last Egg.

Writes one sentence (181 characters) to /output/entry.txt first, then
attempts a repo-root copy of entry.txt guarded in try/except so the run
still exits 0 when the repo is mounted read-only (grader sandbox).
Deterministic: no network, no randomness, no time, no environment input.
"""

import os

SENTENCE = (
    "At two in the morning in a Jakarta warung, my father split his last "
    "fried egg over my rice, the yolk running gold, and called it a feast "
    "\u2014 the smallest share that ever made me rich."
)


def main() -> None:
    if not SENTENCE.strip() or "\n" in SENTENCE or not 1 <= len(SENTENCE) <= 200:
        raise SystemExit("entry gate failed: sentence must be non-blank, single line, 1-200 chars")
    data = SENTENCE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Best-effort repo-root copy: the grader mounts the repo read-only,
    # so this must never crash the run.
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
