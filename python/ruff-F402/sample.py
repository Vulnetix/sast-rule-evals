# Sample for Ruff rule F402: import-shadowed-by-loop-var
# This file is designed to trigger the F402 rule.
# Run: ruff check --select F402 <this_file>

from os import path

for path in files:
    print(path)
