# Sample for Ruff rule FURB187: list-reverse-copy
# This file is designed to trigger the FURB187 rule.
# Run: ruff check --select FURB187 <this_file>

items = [3, 1, 2]
rev = list(reversed(items))  # FURB187: use [::-1]

