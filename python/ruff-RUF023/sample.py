# Sample for Ruff rule RUF023: unsorted-dunder-slots
# This file is designed to trigger the RUF023 rule.
# Run: ruff check --select RUF023 <this_file>

class Dog:
    __slots__ = "name", "breed"
