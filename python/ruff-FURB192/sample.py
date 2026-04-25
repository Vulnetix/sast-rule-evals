# Sample for Ruff rule FURB192: sorted-min-max
# This file is designed to trigger the FURB192 rule.
# Run: ruff check --select FURB192 <this_file>

items = [3, 1, 4, 1, 5]
largest = sorted(items, reverse=True)[0]  # FURB192: use max()

