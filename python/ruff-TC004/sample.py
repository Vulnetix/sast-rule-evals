# Sample for Ruff rule TC004: runtime-import-in-type-checking-block
# This file is designed to trigger the TC004 rule.
# Run: ruff check --select TC004 <this_file>

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import foo


def bar() -> None:
    foo.bar()  # raises NameError: name 'foo' is not defined
