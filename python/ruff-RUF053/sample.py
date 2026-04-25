# Sample for Ruff rule RUF053: class-with-mixed-type-vars
# This file is designed to trigger the RUF053 rule.
# Run: ruff check --select RUF053 <this_file>

from typing import Generic, TypeVar

U = TypeVar("U")

# TypeError: Cannot inherit from Generic[...] multiple times.
class C[T](Generic[U]): ...
