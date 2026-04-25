# Sample for Ruff rule PLR0124: comparison-with-itself
# This file is designed to trigger the PLR0124 rule.
# Run: ruff check --select PLR0124 <this_file>

x = 1
if x == x:  # PLR0124: comparing to itself
    pass

