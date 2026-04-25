# Sample for Ruff rule FURB132: check-and-remove-from-set
# This file is designed to trigger the FURB132 rule.
# Run: ruff check --select FURB132 <this_file>

if item in my_set:
    my_set.remove(item)  # FURB132: use discard()

