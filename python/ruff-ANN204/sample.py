# Sample for Ruff rule ANN204: missing-return-type-special-method
# This file is designed to trigger the ANN204 rule.
# Run: ruff check --select ANN204 <this_file>

class Foo:
    def __init__(self, x: int):
        self.x = x
