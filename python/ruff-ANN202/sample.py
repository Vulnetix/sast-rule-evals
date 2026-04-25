# Sample for Ruff rule ANN202: missing-return-type-private-function
# This file is designed to trigger the ANN202 rule.
# Run: ruff check --select ANN202 <this_file>

def _add(a, b):
    return a + b
