# Sample for Ruff rule N805: invalid-first-argument-name-for-method
# This file is designed to trigger the N805 rule.
# Run: ruff check --select N805 <this_file>

class MyClass:
    def process(this):  # N805: should be self
        pass

