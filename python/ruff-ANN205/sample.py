# Sample for Ruff rule ANN205: missing-return-type-static-method
# This file is designed to trigger the ANN205 rule.
# Run: ruff check --select ANN205 <this_file>

class Foo:
    @staticmethod
    def bar():
        return 1
