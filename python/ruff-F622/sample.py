# Sample for Ruff rule F622: multiple-starred-expressions
# This file is designed to trigger the F622 rule.
# Run: ruff check --select F622 <this_file>

*foo, *bar, baz = (1, 2, 3)
