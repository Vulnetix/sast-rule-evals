# Sample for Ruff rule SIM110: reimplemented-builtin
# This file is designed to trigger the SIM110 rule.
# Run: ruff check --select SIM110 <this_file>

def foo():
    for item in iterable:
        if predicate(item):
            return True
    return False
