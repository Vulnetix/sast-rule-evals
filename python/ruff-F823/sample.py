# Sample for Ruff rule F823: undefined-local
# This file is designed to trigger the F823 rule.
# Run: ruff check --select F823 <this_file>

x = 1


def foo():
    x += 1
