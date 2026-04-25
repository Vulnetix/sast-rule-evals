# Sample for Ruff rule RET504: unnecessary-assign
# This file is designed to trigger the RET504 rule.
# Run: ruff check --select RET504 <this_file>

def calculate(x):
    result = x * 2
    return result  # RET504: unnecessary assignment

