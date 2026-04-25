# Sample for Ruff rule F901: raise-not-implemented
# This file is designed to trigger the F901 rule.
# Run: ruff check --select F901 <this_file>

class Foo:
    def bar(self):
        raise NotImplemented
