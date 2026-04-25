# Sample for Ruff rule FURB129: readlines-in-for
# This file is designed to trigger the FURB129 rule.
# Run: ruff check --select FURB129 <this_file>

with open("file.txt") as fp:
    for line in fp.readlines():
        ...
