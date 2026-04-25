# Sample for Ruff rule TC007: unquoted-type-alias
# This file is designed to trigger the TC007 rule.
# Run: ruff check --select TC007 <this_file>

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from foo import Foo
OptFoo: TypeAlias = Foo | None
