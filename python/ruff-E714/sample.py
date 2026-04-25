# Sample for Ruff rule E714: not-is-test
# This file is designed to trigger the E714 rule.
# Run: ruff check --select E714 <this_file>

if not X is Y:
    pass
Z = not X.B is Y
