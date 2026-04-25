# Sample for Ruff rule D107: undocumented-public-init
# This file is designed to trigger the D107 rule.
# Run: ruff check --select D107 <this_file>

class City:
    def __init__(self, name: str, population: int) -> None:
        self.name: str = name
        self.population: int = population
