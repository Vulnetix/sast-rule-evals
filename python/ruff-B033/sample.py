# Sample for Ruff rule B033: duplicate-value
# This file is designed to trigger the B033 rule.
# Run: ruff check --select B033 <this_file>

s = {1, 2, 2, 3}  # B033: duplicate in set literal

