# Sample for Ruff rule ERA001: commented-out-code
# This file is designed to trigger the ERA001 rule.
# Run: ruff check --select ERA001 <this_file>

def foo():
    # import os
    # return x
    x = 1
    return x

