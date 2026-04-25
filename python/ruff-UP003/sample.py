# Sample for Ruff rule UP003: type-of-primitive
# This file is designed to trigger the UP003 rule.
# Run: ruff check --select UP003 <this_file>

if type(x) is int:  # UP003: use isinstance()
    pass

