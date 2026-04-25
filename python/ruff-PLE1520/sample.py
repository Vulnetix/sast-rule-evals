# Sample for Ruff rule PLE1520: singledispatchmethod-function
# This file is designed to trigger the PLE1520 rule.
# Run: ruff check --select PLE1520 <this_file>

from functools import singledispatchmethod


@singledispatchmethod
def func(arg): ...
