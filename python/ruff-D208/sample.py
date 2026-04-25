# Sample for Ruff rule D208: over-indentation
# This file is designed to trigger the D208 rule.
# Run: ruff check --select D208 <this_file>

def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.

        Sort the list in ascending order and return a copy of the result using the
        bubble sort algorithm.
    """
