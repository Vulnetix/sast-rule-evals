# Sample for Ruff rule DOC201: docstring-missing-returns
# This file is designed to trigger the DOC201 rule.
# Run: ruff check --select DOC201 <this_file>

def get_items():
    """Get a list of items."""
    return [1, 2, 3]  # DOC201: missing Returns in docstring

