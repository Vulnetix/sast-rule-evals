# Sample for Ruff rule PLE0117: nonlocal-without-binding
# This file is designed to trigger the PLE0117 rule.
# Run: ruff check --select PLE0117 <this_file>

def foo():
    nonlocal x  # PLE0117: no enclosing scope
    x = 1

