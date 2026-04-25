# Sample for Ruff rule PYI001: unprefixed-type-param
# This file is designed to trigger the PYI001 rule.
# Run: ruff check --select PYI001 <this_file>

def foo(x, y) -> None:  # PYI001: missing annotation in stub
    ...

