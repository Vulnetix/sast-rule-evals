# Sample for Ruff rule PYI064: redundant-final-literal
# This file is designed to trigger the PYI064 rule.
# Run: ruff check --select PYI064 <this_file>

from typing import Final
x: Final[None] = None  # PYI064: just use None

