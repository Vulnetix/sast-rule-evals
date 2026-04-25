# Sample for Ruff rule PYI007: unrecognized-platform-check
# This file is designed to trigger the PYI007 rule.
# Run: ruff check --select PYI007 <this_file>

from typing import overload

@overload
def process(x: int) -> int: ...
def process(x):  # PYI007: overload with implementation
    return x

