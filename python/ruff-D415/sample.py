# Sample for Ruff rule D415: missing-terminal-punctuation
# This file is designed to trigger the D415 rule.
# Run: ruff check --select D415 <this_file>

def average(values: list[float]) -> float:
    """Return the mean of the given values"""
