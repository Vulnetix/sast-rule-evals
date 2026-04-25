# Sample for Ruff rule RUF052: used-dummy-variable
# This file is designed to trigger the RUF052 rule.
# Run: ruff check --select RUF052 <this_file>

def function():
    _variable = 3
    # important: avoid shadowing the builtin `id()` function!
    _id = 4
    return _variable + _id
