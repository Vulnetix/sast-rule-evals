# Sample for Ruff rule D420: incorrect-section-order
# This file is designed to trigger the D420 rule.
# Run: ruff check --select D420 <this_file>

def func() -> int:
    """Summary.

    Notes
    -----
    Some notes.

    Returns
    -------
    int
    """
