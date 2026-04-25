# Sample for Ruff rule FURB131: delete-full-slice
# This file is designed to trigger the FURB131 rule.
# Run: ruff check --select FURB131 <this_file>

items = [1, 2, 3]
del items[:]  # FURB131: use .clear()

