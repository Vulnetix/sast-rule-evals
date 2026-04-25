# Sample for Ruff rule PLW0127: self-assigning-variable
# This file is designed to trigger the PLW0127 rule.
# Run: ruff check --select PLW0127 <this_file>

a = b = 1  # PLW0128: chained assignment
x, x = 1, 2  # PLW0127: self-assignment

