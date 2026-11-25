"""Make the AI Judge Laugh — office joke entry.

Writes one line about office life to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = "I CC'd myself on 312 emails to look busy, then spent 47 minutes reading my own CCs and flagged 3 of them as urgent."


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate range"
    assert ENTRY.strip(), "entry is whitespace only"
    assert "\n" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
