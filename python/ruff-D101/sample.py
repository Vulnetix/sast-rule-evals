# Sample for Ruff rule D101: undocumented-public-class
# This file is designed to trigger the D101 rule.
# Run: ruff check --select D101 <this_file>

class Player:
    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points

    def add_points(self, points: int) -> None:
        self.points += points
