# Sample for Ruff rule F722: forward-annotation-syntax-error
# This file is designed to trigger the F722 rule.
# Run: ruff check --select F722 <this_file>

def foo() -> "/": ...
