# Sample for Ruff rule RUF005: collection-literal-concatenation
# This file is designed to trigger the RUF005 rule.
# Run: ruff check --select RUF005 <this_file>

a = [1, 2]
b = [3, 4]
c = a + b  # RUF005: use [*a, *b]

