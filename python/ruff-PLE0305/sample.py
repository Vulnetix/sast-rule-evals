# Sample for Ruff rule PLE0305: invalid-index-return-type
# This file is designed to trigger the PLE0305 rule.
# Run: ruff check --select PLE0305 <this_file>

class Foo:
    def __index__(self):
        return "2"
