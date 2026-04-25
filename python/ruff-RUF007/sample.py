# Sample for Ruff rule RUF007: zip-instead-of-pairwise
# This file is designed to trigger the RUF007 rule.
# Run: ruff check --select RUF007 <this_file>

letters = "ABCD"
zip(letters, letters[1:])  # ("A", "B"), ("B", "C"), ("C", "D")
