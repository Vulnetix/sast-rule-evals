# Sample for Ruff rule RUF070: unnecessary-assign-before-yield
# This file is designed to trigger the RUF070 rule.
# Run: ruff check --select RUF070 <this_file>

def gen():
    x = 1
    yield x
