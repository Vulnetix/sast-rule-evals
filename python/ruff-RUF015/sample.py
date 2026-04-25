# Sample for Ruff rule RUF015: unnecessary-iterable-allocation-for-first-element
# This file is designed to trigger the RUF015 rule.
# Run: ruff check --select RUF015 <this_file>

items = [1, 2, 3]
first = next(iter(items))  # RUF015: prefer items[0] or similar

