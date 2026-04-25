# Sample for Ruff rule FURB101: read-whole-file
# This file is designed to trigger the FURB101 rule.
# Run: ruff check --select FURB101 <this_file>

with open("file.txt") as f:
    contents = f.read()
