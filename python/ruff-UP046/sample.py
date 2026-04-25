# Sample for Ruff rule UP046: non-pep695-generic-class
# This file is designed to trigger the UP046 rule.
# Run: ruff check --select UP046 <this_file>

from typing import Generic, TypeVar

T = TypeVar("T")


class GenericClass(Generic[T]):
    var: T
