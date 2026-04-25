# Sample for Ruff rule UP004: useless-object-inheritance
# This file is designed to trigger the UP004 rule.
# Run: ruff check --select UP004 <this_file>

class Foo(object): ...
