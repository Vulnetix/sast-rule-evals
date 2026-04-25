# Sample for Ruff rule ANN002: missing-type-args
# This file is designed to trigger the ANN002 rule.
# Run: ruff check --select ANN002 <this_file>

def foo(*args): ...
