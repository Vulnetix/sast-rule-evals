# Sample for Ruff rule PLC0131: type-bivariance
# This file is designed to trigger the PLC0131 rule.
# Run: ruff check --select PLC0131 <this_file>

from typing import TypeVar

T = TypeVar("T", covariant=True, contravariant=True)
