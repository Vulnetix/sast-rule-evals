# Sample for Ruff rule E251: unexpected-spaces-around-keyword-parameter-equals
# This file is designed to trigger the E251 rule.
# Run: ruff check --select E251 <this_file>

def add(a = 0) -> int:
    return a + 1
