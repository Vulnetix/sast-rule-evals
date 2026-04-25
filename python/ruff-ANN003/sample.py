# Sample for Ruff rule ANN003: missing-type-kwargs
# This file is designed to trigger the ANN003 rule.
# Run: ruff check --select ANN003 <this_file>

def foo(**kwargs): ...
