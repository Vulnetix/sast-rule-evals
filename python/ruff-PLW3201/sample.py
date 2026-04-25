# Sample for Ruff rule PLW3201: bad-dunder-method-name
# This file is designed to trigger the PLW3201 rule.
# Run: ruff check --select PLW3201 <this_file>

class Foo:
    def __init_(self): ...
