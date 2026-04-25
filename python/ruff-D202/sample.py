# Sample for Ruff rule D202: blank-line-after-function
# This file is designed to trigger the D202 rule.
# Run: ruff check --select D202 <this_file>

def average(values: list[float]) -> float:
    """Return the mean of the given values."""

    return sum(values) / len(values)
