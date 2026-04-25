# Sample for Ruff rule D201: blank-line-before-function
# This file is designed to trigger the D201 rule.
# Run: ruff check --select D201 <this_file>

def average(values: list[float]) -> float:

    """Return the mean of the given values."""
