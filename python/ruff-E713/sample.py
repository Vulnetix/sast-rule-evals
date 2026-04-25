# Sample for Ruff rule E713: not-in-test
# This file is designed to trigger the E713 rule.
# Run: ruff check --select E713 <this_file>

Z = not X in Y
if not X.B in Y:
    pass
