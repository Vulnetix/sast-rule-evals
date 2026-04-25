# Sample for Ruff rule PLR1730: if-stmt-min-max
# This file is designed to trigger the PLR1730 rule.
# Run: ruff check --select PLR1730 <this_file>

if score > highest_score:
    highest_score = score
