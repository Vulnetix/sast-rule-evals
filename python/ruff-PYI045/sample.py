# Sample for Ruff rule PYI045: iter-method-return-iterable
# This file is designed to trigger the PYI045 rule.
# Run: ruff check --select PYI045 <this_file>

from typing import Iterator, Iterable

class MyCollection:
    def __iter__(self) -> Iterable[int]:  # PYI045: should be Iterator
        yield 1

