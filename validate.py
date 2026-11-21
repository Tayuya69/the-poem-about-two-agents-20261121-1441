#!/usr/bin/env python3
"""Local validator for the poem entry.

Runs main.py into a temp dir and asserts the make.fun gate conditions:
entry.txt exists, is valid UTF-8, 1-280 Unicode code points, and not
only whitespace. Prints the char count and the poem.
"""

import os
import subprocess
import sys
import tempfile


def main() -> None:
    repo = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        subprocess.run(
            [sys.executable, os.path.join(repo, "main.py")],
            env=env,
            check=True,
        )
        path = os.path.join(tmp, "entry.txt")
        assert os.path.isfile(path), "entry.txt was not created"
        with open(path, encoding="utf-8") as f:
            text = f.read()
        chars = len(text)
        assert text.strip(), "entry.txt is only whitespace"
        assert 1 <= chars <= 280, f"entry.txt is {chars} chars, must be 1-280"
        print(f"OK: entry.txt is {chars} characters")
        print("---")
        print(text)


if __name__ == "__main__":
    main()
