# Sample for Ruff rule FURB105: print-empty-string
# This file is designed to trigger the FURB105 rule.
# Run: ruff check --select FURB105 <this_file>

parts = ["a", "b", "c"]
result = "".join([p.upper() for p in parts])  # FURB105: unnecessary list

