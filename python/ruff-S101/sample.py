# Sample for Ruff rule S101: assert
# This file is designed to trigger the S101 rule.
# Run: ruff check --select S101 <this_file>

def check(value):
    assert value > 0  # S101: assert in production code
    return value

