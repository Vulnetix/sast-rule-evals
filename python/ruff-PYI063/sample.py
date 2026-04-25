# Sample for Ruff rule PYI063: pep484-style-positional-only-parameter
# This file is designed to trigger the PYI063 rule.
# Run: ruff check --select PYI063 <this_file>

class Foo:
    def method(self) -> "Foo":  # PYI063: use Self
        return self

