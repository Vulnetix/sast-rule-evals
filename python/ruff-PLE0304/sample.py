# Sample for Ruff rule PLE0304: invalid-bool-return-type
# This file is designed to trigger the PLE0304 rule.
# Run: ruff check --select PLE0304 <this_file>

class Foo:
    def __bool__(self):
        return 2
