# Sample for Ruff rule RUF033: post-init-default
# This file is designed to trigger the RUF033 rule.
# Run: ruff check --select RUF033 <this_file>

from dataclasses import InitVar, dataclass


@dataclass
class Foo:
    bar: InitVar[int] = 0

    def __post_init__(self, bar: int = 1, baz: int = 2) -> None:
        print(bar, baz)


foo = Foo()  # Prints '0 2'.
