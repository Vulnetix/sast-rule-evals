# Sample for Ruff rule FURB103: write-whole-file
# This file is designed to trigger the FURB103 rule.
# Run: ruff check --select FURB103 <this_file>

with open("file.txt", "w") as f:
    f.write("some text")
