# Sample for Ruff rule F704: yield-outside-function
# This file is designed to trigger the F704 rule.
# Run: ruff check --select F704 <this_file>

class Foo:
    yield 1
