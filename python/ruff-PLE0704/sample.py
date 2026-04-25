# Sample for Ruff rule PLE0704: misplaced-bare-raise
# This file is designed to trigger the PLE0704 rule.
# Run: ruff check --select PLE0704 <this_file>

from typing import Any


def is_some(obj: Any) -> bool:
    if obj is None:
        raise
