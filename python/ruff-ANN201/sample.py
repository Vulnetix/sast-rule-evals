# Sample for Ruff rule ANN201: missing-return-type-undocumented-public-function
# This file is designed to trigger the ANN201 rule.
# Run: ruff check --select ANN201 <this_file>

def get_name():  # ANN201: missing return type
    return "Alice"

