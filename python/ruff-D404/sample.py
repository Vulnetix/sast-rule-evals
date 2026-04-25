# Sample for Ruff rule D404: docstring-starts-with-this
# This file is designed to trigger the D404 rule.
# Run: ruff check --select D404 <this_file>

def average(values: list[float]) -> float:
    """This function returns the mean of the given values."""
