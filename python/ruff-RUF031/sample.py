# Sample for Ruff rule RUF031: incorrectly-parenthesized-tuple-in-subscript
# This file is designed to trigger the RUF031 rule.
# Run: ruff check --select RUF031 <this_file>

directions = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}
directions[(0, 1)]
