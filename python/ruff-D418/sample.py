# Sample for Ruff rule D418: overload-with-docstring
# This file is designed to trigger the D418 rule.
# Run: ruff check --select D418 <this_file>

from typing import overload


@overload
def factorial(n: int) -> int:
    """Return the factorial of n."""


@overload
def factorial(n: float) -> float:
    """Return the factorial of n."""


def factorial(n):
    """Return the factorial of n."""


factorial.__doc__  # "Return the factorial of n."
