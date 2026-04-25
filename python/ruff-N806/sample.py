# Sample for Ruff rule N806: non-lowercase-variable-in-function
# This file is designed to trigger the N806 rule.
# Run: ruff check --select N806 <this_file>

def calculate():
    TotalAmount = 100  # N806: variable should be lowercase
    return TotalAmount

