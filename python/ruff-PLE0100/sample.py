# Sample for Ruff rule PLE0100: yield-in-init
# This file is designed to trigger the PLE0100 rule.
# Run: ruff check --select PLE0100 <this_file>

class InitIsGenerator:
    def __init__(self, i):
        yield i
