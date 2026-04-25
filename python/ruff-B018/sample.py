# Sample for Ruff rule B018: useless-expression
# This file is designed to trigger the B018 rule.
# Run: ruff check --select B018 <this_file>

class Foo:
    "not a real docstring"  # B018: useless expression
    x = 1

