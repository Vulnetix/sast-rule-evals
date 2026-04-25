# Sample for Ruff rule E721: type-comparison
# This file is designed to trigger the E721 rule.
# Run: ruff check --select E721 <this_file>

if type(x) == int:  # E721: use isinstance()
    pass

