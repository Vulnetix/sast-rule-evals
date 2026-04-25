# Sample for Ruff rule PIE796: non-unique-enums
# This file is designed to trigger the PIE796 rule.
# Run: ruff check --select PIE796 <this_file>

from enum import Enum


class Foo(Enum):
    A = 1
    B = 2
    C = 1
