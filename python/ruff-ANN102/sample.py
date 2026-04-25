# Sample for Ruff rule ANN102: missing-type-cls
# This file is designed to trigger the ANN102 rule.
# Run: ruff check --select ANN102 <this_file>

class Foo:
    @classmethod
    def bar(cls): ...
