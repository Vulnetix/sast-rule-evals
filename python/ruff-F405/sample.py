# Sample for Ruff rule F405: undefined-local-with-import-star-usage
# This file is designed to trigger the F405 rule.
# Run: ruff check --select F405 <this_file>

from math import *


def area(radius):
    return pi * radius**2
