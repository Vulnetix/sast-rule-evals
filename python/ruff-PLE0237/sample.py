# Sample for Ruff rule PLE0237: non-slot-assignment
# This file is designed to trigger the PLE0237 rule.
# Run: ruff check --select PLE0237 <this_file>

class Student:
    __slots__ = ("name",)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  # [assigning-non-slot]
        self.setup()

    def setup(self):
        pass
