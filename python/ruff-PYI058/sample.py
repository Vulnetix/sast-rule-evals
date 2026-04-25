# Sample for Ruff rule PYI058: generator-return-from-iter-method
# This file is designed to trigger the PYI058 rule.
# Run: ruff check --select PYI058 <this_file>

from collections.abc import AsyncGenerator, Generator
from typing import Any


class CustomIterator:
    def __iter__(self) -> Generator:
        yield from range(42)


class CustomIterator2:
    def __iter__(self) -> Generator[str, Any, None]:
        yield from "abcdefg"
