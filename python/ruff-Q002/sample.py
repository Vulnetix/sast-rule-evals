# Sample for Ruff rule Q002: bad-quotes-docstring
# This file is designed to trigger the Q002 rule.
# Run: ruff check --select Q002 <this_file>

def foo():
    '''This is a docstring.'''  # Q002: single-quote docstring
    pass

