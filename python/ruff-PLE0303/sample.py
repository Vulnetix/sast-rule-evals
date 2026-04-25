# Sample for Ruff rule PLE0303: invalid-length-return-type
# This file is designed to trigger the PLE0303 rule.
# Run: ruff check --select PLE0303 <this_file>

class Foo:
    def __len__(self):
        return "2"
