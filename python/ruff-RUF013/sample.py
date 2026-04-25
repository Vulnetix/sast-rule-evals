# Sample for Ruff rule RUF013: implicit-optional
# This file is designed to trigger the RUF013 rule.
# Run: ruff check --select RUF013 <this_file>

from typing import Optional

def foo(x: Optional[str] = None) -> None:  # RUF013: use str | None
    pass

