# Sample for Ruff rule TRY002: raise-vanilla-class
# This file is designed to trigger the TRY002 rule.
# Run: ruff check --select TRY002 <this_file>

def validate(x):
    if x < 0:
        raise Exception("Value must be positive")  # TRY002: use custom exception

