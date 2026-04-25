# Sample for Ruff rule PT028: pytest-parameter-with-default-argument
# This file is designed to trigger the PT028 rule.
# Run: ruff check --select PT028 <this_file>

def test_foo(a=1): ...
