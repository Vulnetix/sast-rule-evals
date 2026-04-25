# Sample for Ruff rule PLE0101: return-in-init
# This file is designed to trigger the PLE0101 rule.
# Run: ruff check --select PLE0101 <this_file>

class Example:
    def __init__(self):
        return []
