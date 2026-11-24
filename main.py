"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one line (<=120 chars) to <output dir>/entry.txt.
The output dir is MAKEFUN_OUTPUT_DIR when set, else /output.
Standard library only.
"""

import os

FORTUNE = (
    "Soon your newest leaf will unfurl toward the morning sun — "
    "and the whole windowsill will gossip about your bravery."
)


def main() -> None:
    # Gate: exactly one line, 1-120 characters, not only whitespace.
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} chars"
    assert "\n" not in FORTUNE and FORTUNE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
