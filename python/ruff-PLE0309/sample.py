# Sample for Ruff rule PLE0309: invalid-hash-return-type
# This file is designed to trigger the PLE0309 rule.
# Run: ruff check --select PLE0309 <this_file>

class Foo:
    def __hash__(self):
        return "2"
