# Sample for Ruff rule RUF012: mutable-class-default
# This file is designed to trigger the RUF012 rule.
# Run: ruff check --select RUF012 <this_file>

class MyModel:
    items = []  # RUF012: mutable class attr without ClassVar
    data = {}

