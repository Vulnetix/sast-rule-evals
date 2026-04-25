# Sample for Ruff rule PYI042: snake-case-type-alias
# This file is designed to trigger the PYI042 rule.
# Run: ruff check --select PYI042 <this_file>

from typing import TypeVar
myTypeVar = TypeVar("myTypeVar")  # PYI042: should be CamelCase

