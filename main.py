#!/usr/bin/env python3
"""One Star, Five Stars for the Food - make.fun entry.

Writes a single-sentence alien tourist review of Earth to entry.txt.
Stdlib only, no network, fully deterministic.
"""

from pathlib import Path

SENTENCE = (
    "One star: the sky tried to poison me, the gravity is a suggestion, "
    "and the locals worship glowing rectangles, but the pork dumplings "
    "alone were worth the nine-light-year flight."
)


def main() -> None:
    output_dir = Path(__import__("os").environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(SENTENCE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
