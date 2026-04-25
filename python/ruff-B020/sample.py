# Sample for Ruff rule B020: loop-variable-overrides-iterator
# This file is designed to trigger the B020 rule.
# Run: ruff check --select B020 <this_file>

items = [1, 2, 3]
for item in items:
    items[0] = item  # B020: modifying iterable

