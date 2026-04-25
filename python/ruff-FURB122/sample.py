# Sample for Ruff rule FURB122: for-loop-writes
# This file is designed to trigger the FURB122 rule.
# Run: ruff check --select FURB122 <this_file>

from pathlib import Path

with Path("file").open("w") as f:
    for line in lines:
        f.write(line)

with Path("file").open("wb") as f_b:
    for line_b in lines_b:
        f_b.write(line_b.encode())
