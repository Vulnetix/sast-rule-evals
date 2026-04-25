# Sample for Ruff rule D401: non-imperative-mood
# This file is designed to trigger the D401 rule.
# Run: ruff check --select D401 <this_file>

def average(values: list[float]) -> float:
    """Returns the mean of the given values."""
