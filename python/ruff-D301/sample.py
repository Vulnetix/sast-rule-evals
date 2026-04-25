# Sample for Ruff rule D301: escape-sequence-in-docstring
# This file is designed to trigger the D301 rule.
# Run: ruff check --select D301 <this_file>

def foobar():
    """Docstring for foo\bar."""


foobar.__doc__  # "Docstring for foar."
