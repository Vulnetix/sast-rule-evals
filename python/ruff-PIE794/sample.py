# Sample for Ruff rule PIE794: duplicate-class-field-definition
# This file is designed to trigger the PIE794 rule.
# Run: ruff check --select PIE794 <this_file>

class Person:
    name = Tom
    ...
    name = Ben
