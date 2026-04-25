# Sample for Ruff rule B005: strip-with-multi-characters
# This file is designed to trigger the B005 rule.
# Run: ruff check --select B005 <this_file>

"text.txt".strip(".txt")  # "e"
