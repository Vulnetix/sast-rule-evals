# Sample for Ruff rule B021: f-string-docstring
# This file is designed to trigger the B021 rule.
# Run: ruff check --select B021 <this_file>

def foo():
    """This does {thing}."""  # B021: f-string in docstring?
    pass

