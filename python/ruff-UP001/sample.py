# Sample for Ruff rule UP001: useless-metaclass-type
# This file is designed to trigger the UP001 rule.
# Run: ruff check --select UP001 <this_file>

class Foo:
    __metaclass__ = type
