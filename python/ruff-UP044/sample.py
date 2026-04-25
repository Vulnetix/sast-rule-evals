# Sample for Ruff rule UP044: non-pep646-unpack
# This file is designed to trigger the UP044 rule.
# Run: ruff check --select UP044 <this_file>

from typing import Unpack


def foo(*args: Unpack[tuple[int, ...]]) -> None:
    pass
