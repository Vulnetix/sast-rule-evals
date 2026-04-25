# Sample for Ruff rule D402: signature-in-docstring
# This file is designed to trigger the D402 rule.
# Run: ruff check --select D402 <this_file>

def foo(a, b):
    """foo(a: int, b: int) -> list[int]"""
