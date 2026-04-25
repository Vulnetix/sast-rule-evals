# Sample for Ruff rule E252: missing-whitespace-around-parameter-equals
# This file is designed to trigger the E252 rule.
# Run: ruff check --select E252 <this_file>

def add(a: int=0) -> int:
    return a + 1
