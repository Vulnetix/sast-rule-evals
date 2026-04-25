# Sample for Ruff rule D200: unnecessary-multiline-docstring
# This file is designed to trigger the D200 rule.
# Run: ruff check --select D200 <this_file>

def average(values: list[float]) -> float:
    """
    Return the mean of the given values.
    """
