# Sample for Ruff rule PLC0132: type-param-name-mismatch
# This file is designed to trigger the PLC0132 rule.
# Run: ruff check --select PLC0132 <this_file>

from typing import TypeVar

T = TypeVar("U")
