# Sample for Ruff rule UP047: non-pep695-generic-function
# This file is designed to trigger the UP047 rule.
# Run: ruff check --select UP047 <this_file>

from typing import TypeVar

T = TypeVar("T")


def generic_function(var: T) -> T:
    return var
