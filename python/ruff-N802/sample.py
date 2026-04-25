# Sample for Ruff rule N802: invalid-function-name
# This file is designed to trigger the N802 rule.
# Run: ruff check --select N802 <this_file>

def MyFunction():  # N802: should be my_function
    pass

