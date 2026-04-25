# Sample for Ruff rule ARG003: unused-class-method-argument
# This file is designed to trigger the ARG003 rule.
# Run: ruff check --select ARG003 <this_file>

class Foo:
    @classmethod
    def create(cls, unused):  # ARG003: unused classmethod arg
        return cls()

