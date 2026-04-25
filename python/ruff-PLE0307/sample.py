# Sample for Ruff rule PLE0307: invalid-str-return-type
# This file is designed to trigger the PLE0307 rule.
# Run: ruff check --select PLE0307 <this_file>

class Foo:
    def __str__(self):
        return True
