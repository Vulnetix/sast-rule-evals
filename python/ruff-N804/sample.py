# Sample for Ruff rule N804: invalid-first-argument-name-for-class-method
# This file is designed to trigger the N804 rule.
# Run: ruff check --select N804 <this_file>

class MyClass:
    @classmethod
    def create(self):  # N804: should be cls
        return MyClass()

