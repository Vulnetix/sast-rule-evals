# Sample for Ruff rule F842: unused-annotation
# This file is designed to trigger the F842 rule.
# Run: ruff check --select F842 <this_file>

def foo():
    bar: int
