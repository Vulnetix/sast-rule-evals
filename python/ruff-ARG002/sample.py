# Sample for Ruff rule ARG002: unused-method-argument
# This file is designed to trigger the ARG002 rule.
# Run: ruff check --select ARG002 <this_file>

class Foo:
    def process(self, unused):  # ARG002: unused method arg
        return 42

