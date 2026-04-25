# Sample for Ruff rule TRY003: raise-vanilla-args
# This file is designed to trigger the TRY003 rule.
# Run: ruff check --select TRY003 <this_file>

def validate(x):
    if x < 0:
        raise ValueError("This value cannot be negative, please provide a positive integer")  # TRY003

