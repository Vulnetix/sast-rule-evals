# Sample for Ruff rule RUF017: quadratic-list-summation
# This file is designed to trigger the RUF017 rule.
# Run: ruff check --select RUF017 <this_file>

total = sum([1, 2, 3])  # RUF017: list not needed in sum()

