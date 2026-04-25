# Sample for Ruff rule N815: mixed-case-variable-in-class-scope
# This file is designed to trigger the N815 rule.
# Run: ruff check --select N815 <this_file>

class Foo:
    myValue = 1  # N815: mixedCase in class scope

