# Sample for Ruff rule F406: undefined-local-with-nested-import-star-usage
# This file is designed to trigger the F406 rule.
# Run: ruff check --select F406 <this_file>

def foo():
    from math import *
