# Sample for Ruff rule UP015: redundant-open-modes
# This file is designed to trigger the UP015 rule.
# Run: ruff check --select UP015 <this_file>

with open("file.txt", "r") as f:  # UP015: unnecessary "r"
    content = f.read()

