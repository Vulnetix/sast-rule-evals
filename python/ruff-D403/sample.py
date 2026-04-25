# Sample for Ruff rule D403: first-word-uncapitalized
# This file is designed to trigger the D403 rule.
# Run: ruff check --select D403 <this_file>

def average(values: list[float]) -> float:
    """return the mean of the given values."""
