# Sample for Ruff rule D209: new-line-after-last-paragraph
# This file is designed to trigger the D209 rule.
# Run: ruff check --select D209 <this_file>

def sort_list(l: List[int]) -> List[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm."""
