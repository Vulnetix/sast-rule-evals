# Sample for Ruff rule F821: undefined-name
# This file is designed to trigger the F821 rule.
# Run: ruff check --select F821 <this_file>

def double():
    return n * 2  # raises `NameError` if `n` is undefined when `double` is called
