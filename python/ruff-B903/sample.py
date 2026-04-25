# Sample for Ruff rule B903: class-as-data-structure
# This file is designed to trigger the B903 rule.
# Run: ruff check --select B903 <this_file>

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
