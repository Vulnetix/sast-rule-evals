# Sample for Ruff rule PYI061: redundant-none-literal
# This file is designed to trigger the PYI061 rule.
# Run: ruff check --select PYI061 <this_file>

from typing import Literal

Literal[None]
Literal[1, 2, 3, "foo", 5, None]
