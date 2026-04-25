# Sample for Ruff rule PTH123: builtin-open
# This file is designed to trigger the PTH123 rule.
# Run: ruff check --select PTH123 <this_file>

with open("file.txt") as f:  # PTH123
    data = f.read()

