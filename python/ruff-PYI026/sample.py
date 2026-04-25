# Sample for Ruff rule PYI026: type-alias-without-annotation
# This file is designed to trigger the PYI026 rule.
# Run: ruff check --select PYI026 <this_file>

from typing import TypeAlias
MyType: TypeAlias = int  # PYI026: use 'type' statement (py3.12+)

