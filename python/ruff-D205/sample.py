# Sample for Ruff rule D205: missing-blank-line-after-summary
# This file is designed to trigger the D205 rule.
# Run: ruff check --select D205 <this_file>

def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the
    result using the bubble sort algorithm.
    """
