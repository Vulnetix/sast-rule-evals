# Sample for Ruff rule RUF021: parenthesize-chained-operators
# This file is designed to trigger the RUF021 rule.
# Run: ruff check --select RUF021 <this_file>

a, b, c = 1, 0, 2
x = a or b and c

d, e, f = 0, 1, 2
y = d and e or f
