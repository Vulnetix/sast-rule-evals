# Sample for Ruff rule UP040: non-pep695-type-alias
# This file is designed to trigger the UP040 rule.
# Run: ruff check --select UP040 <this_file>

from typing import Annotated, TypeAlias, TypeAliasType
from annotated_types import Gt

ListOfInt: TypeAlias = list[int]
PositiveInt = TypeAliasType("PositiveInt", Annotated[int, Gt(0)])
