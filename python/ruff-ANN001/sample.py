# Sample for Ruff rule ANN001: missing-type-function-argument
# This file is designed to trigger the ANN001 rule.
# Run: ruff check --select ANN001 <this_file>

def greet(name):  # ANN001: missing annotation
    return f"Hello, {name}"

