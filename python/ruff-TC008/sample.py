# Sample for Ruff rule TC008: quoted-type-alias
# This file is designed to trigger the TC008 rule.
# Run: ruff check --select TC008 <this_file>

from typing import TypeAlias

OptInt: TypeAlias = "int | None"
