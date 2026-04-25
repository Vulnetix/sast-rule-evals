# Sample for Ruff rule RUF020: never-union
# This file is designed to trigger the RUF020 rule.
# Run: ruff check --select RUF020 <this_file>

from typing import Never


def func() -> Never | int: ...
