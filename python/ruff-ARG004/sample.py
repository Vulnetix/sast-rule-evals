# Sample for Ruff rule ARG004: unused-static-method-argument
# This file is designed to trigger the ARG004 rule.
# Run: ruff check --select ARG004 <this_file>

class Foo:
    @staticmethod
    def helper(unused):  # ARG004: unused staticmethod arg
        return 42

