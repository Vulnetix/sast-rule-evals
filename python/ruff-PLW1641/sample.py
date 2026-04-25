# Sample for Ruff rule PLW1641: eq-without-hash
# This file is designed to trigger the PLW1641 rule.
# Run: ruff check --select PLW1641 <this_file>

class Person:
    def __init__(self):
        self.name = "monty"

    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name
