# Sample for Ruff rule ANN101: missing-type-self
# This file is designed to trigger the ANN101 rule.
# Run: ruff check --select ANN101 <this_file>

class Foo:
    def bar(self): ...
