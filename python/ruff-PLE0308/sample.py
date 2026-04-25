# Sample for Ruff rule PLE0308: invalid-bytes-return-type
# This file is designed to trigger the PLE0308 rule.
# Run: ruff check --select PLE0308 <this_file>

class Foo:
    def __bytes__(self):
        return 2
