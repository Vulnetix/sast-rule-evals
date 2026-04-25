# Sample for Ruff rule F403: undefined-local-with-import-star
# This file is designed to trigger the F403 rule.
# Run: ruff check --select F403 <this_file>

from math import *


def area(radius):
    return pi * radius**2
