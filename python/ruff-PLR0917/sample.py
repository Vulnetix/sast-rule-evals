# Sample for Ruff rule PLR0917: too-many-positional-arguments
# This file is designed to trigger the PLR0917 rule.
# Run: ruff check --select PLR0917 <this_file>

def plot(x, y, z, color, mark, add_trendline): ...


plot(1, 2, 3, "r", "*", True)
