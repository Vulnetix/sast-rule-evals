# Sample for Ruff rule PLW0642: self-or-cls-assignment
# This file is designed to trigger the PLW0642 rule.
# Run: ruff check --select PLW0642 <this_file>

class Foo:
    def process(self):
        self = "overwritten"  # PLW0642: reassigning self

