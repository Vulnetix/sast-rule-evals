# Sample for Ruff rule TC005: empty-type-checking-block
# This file is designed to trigger the TC005 rule.
# Run: ruff check --select TC005 <this_file>

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass  # TC005: empty TYPE_CHECKING block

