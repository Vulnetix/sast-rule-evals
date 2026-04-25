# Sample for Ruff rule UP050: useless-class-metaclass-type
# This file is designed to trigger the UP050 rule.
# Run: ruff check --select UP050 <this_file>

class Foo(metaclass=type): ...
