# Sample for Ruff rule PLC0105: type-name-incorrect-variance
# This file is designed to trigger the PLC0105 rule.
# Run: ruff check --select PLC0105 <this_file>

from typing import TypeVar
T = TypeVar("MyT")  # PLC0105: name mismatch

