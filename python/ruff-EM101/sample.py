# Sample for Ruff rule EM101: raw-string-in-exception
# This file is designed to trigger the EM101 rule.
# Run: ruff check --select EM101 <this_file>

def check(value):
    if value < 0:
        raise ValueError("Value must be positive")  # EM101: string literal

