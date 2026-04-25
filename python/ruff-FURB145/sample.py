# Sample for Ruff rule FURB145: slice-copy
# This file is designed to trigger the FURB145 rule.
# Run: ruff check --select FURB145 <this_file>

copy = items[:]  # FURB145: use .copy()

