# Sample for Ruff rule PLW0177: nan-comparison
# This file is designed to trigger the PLW0177 rule.
# Run: ruff check --select PLW0177 <this_file>

if x == float("NaN"):
    pass
