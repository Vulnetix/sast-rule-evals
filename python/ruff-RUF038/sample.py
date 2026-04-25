# Sample for Ruff rule RUF038: redundant-bool-literal
# This file is designed to trigger the RUF038 rule.
# Run: ruff check --select RUF038 <this_file>

from typing import Literal

x: Literal[True, False]
y: Literal[True, False, "hello", "world"]
