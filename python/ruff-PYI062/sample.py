# Sample for Ruff rule PYI062: duplicate-literal-member
# This file is designed to trigger the PYI062 rule.
# Run: ruff check --select PYI062 <this_file>

from typing import Literal
def foo(x: Literal[1, 1, 2]) -> None:  # PYI062: duplicate Literal member
    pass

