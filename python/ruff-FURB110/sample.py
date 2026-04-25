# Sample for Ruff rule FURB110: if-exp-instead-of-or-operator
# This file is designed to trigger the FURB110 rule.
# Run: ruff check --select FURB110 <this_file>

x, y = 1, 2

z = x if x else y
