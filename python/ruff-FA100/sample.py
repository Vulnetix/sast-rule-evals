# Sample for Ruff rule FA100: future-rewritable-type-annotation
# This file is designed to trigger the FA100 rule.
# Run: ruff check --select FA100 <this_file>

from typing import Optional

def foo(x: Optional[str]) -> None:  # FA100: add __future__ annotations
    pass

