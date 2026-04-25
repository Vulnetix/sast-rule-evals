# Sample for Ruff rule D212: multi-line-summary-first-line
# This file is designed to trigger the D212 rule.
# Run: ruff check --select D212 <this_file>

def sort_list(l: list[int]) -> list[int]:
    """
    Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm.
    """
