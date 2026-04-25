# Sample for Ruff rule PLC0205: single-string-slots
# This file is designed to trigger the PLC0205 rule.
# Run: ruff check --select PLC0205 <this_file>

class Person:
    __slots__: str = "name"

    def __init__(self, name: str) -> None:
        self.name = name
