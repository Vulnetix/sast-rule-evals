# Sample for Ruff rule PYI016: duplicate-union-member
# This file is designed to trigger the PYI016 rule.
# Run: ruff check --select PYI016 <this_file>

from typing import Optional
def foo(x: Optional[Optional[str]]) -> None:  # PYI016
    pass

