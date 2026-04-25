# Sample for Ruff rule RUF022: unsorted-dunder-all
# This file is designed to trigger the RUF022 rule.
# Run: ruff check --select RUF022 <this_file>

import sys

__all__ = [
    "b",
    "c",
    "a",
]

if sys.platform == "win32":
    __all__ += ["z", "y"]
