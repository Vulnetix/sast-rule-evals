# Sample for Ruff rule PLW1514: unspecified-encoding
# This file is designed to trigger the PLW1514 rule.
# Run: ruff check --select PLW1514 <this_file>

with open("file.txt") as f:  # PLW1514: missing encoding
    data = f.read()

