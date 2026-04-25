# Sample for Ruff rule EM102: f-string-in-exception
# This file is designed to trigger the EM102 rule.
# Run: ruff check --select EM102 <this_file>

def check(value):
    if value < 0:
        raise ValueError(f"Got {value}, expected positive")  # EM102: f-string

