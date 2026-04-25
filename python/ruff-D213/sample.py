# Sample for Ruff rule D213: multi-line-summary-second-line
# This file is designed to trigger the D213 rule.
# Run: ruff check --select D213 <this_file>

def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm.
    """
