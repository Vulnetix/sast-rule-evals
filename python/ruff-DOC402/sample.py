# Sample for Ruff rule DOC402: docstring-missing-yields
# This file is designed to trigger the DOC402 rule.
# Run: ruff check --select DOC402 <this_file>

def count_to_n(n: int) -> int:
    """Generate integers up to *n*.

    Args:
        n: The number at which to stop counting.
    """
    for i in range(1, n + 1):
        yield i
