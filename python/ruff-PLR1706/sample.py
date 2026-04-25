# Sample for Ruff rule PLR1706: and-or-ternary
# This file is designed to trigger the PLR1706 rule.
# Run: ruff check --select PLR1706 <this_file>

x, y = 1, 2
maximum = x >= y and x or y
