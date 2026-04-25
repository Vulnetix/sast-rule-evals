# Sample for Ruff rule F841: unused-variable
# This file is designed to trigger the F841 rule.
# Run: ruff check --select F841 <this_file>

def foo():
    unused = 42  # F841: assigned but never used
    return 1

