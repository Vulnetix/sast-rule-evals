# Sample for Ruff rule PYI059: generic-not-last-base-class
# This file is designed to trigger the PYI059 rule.
# Run: ruff check --select PYI059 <this_file>

from collections.abc import Container, Iterable, Sized
from typing import Generic, TypeVar


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class LinkedList(Generic[T], Sized):
    def push(self, item: T) -> None:
        self._items.append(item)


class MyMapping(
    Generic[K, V],
    Iterable[tuple[K, V]],
    Container[tuple[K, V]],
):
    ...
