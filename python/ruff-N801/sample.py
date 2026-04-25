# Sample for Ruff rule N801: invalid-class-name
# This file is designed to trigger the N801 rule.
# Run: ruff check --select N801 <this_file>

class myclass:  # N801: should be MyClass
    pass

