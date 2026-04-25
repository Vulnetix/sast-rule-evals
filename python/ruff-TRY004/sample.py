# Sample for Ruff rule TRY004: type-check-without-type-error
# This file is designed to trigger the TRY004 rule.
# Run: ruff check --select TRY004 <this_file>

def foo(n: int):
    if isinstance(n, int):
        pass
    else:
        raise ValueError("n must be an integer")
