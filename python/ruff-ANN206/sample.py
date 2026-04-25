# Sample for Ruff rule ANN206: missing-return-type-class-method
# This file is designed to trigger the ANN206 rule.
# Run: ruff check --select ANN206 <this_file>

class Foo:
    @classmethod
    def bar(cls):
        return 1
