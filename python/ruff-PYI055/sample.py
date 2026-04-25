# Sample for Ruff rule PYI055: unnecessary-type-union
# This file is designed to trigger the PYI055 rule.
# Run: ruff check --select PYI055 <this_file>

from typing import Union
def foo(x: Union[None, int]) -> None:  # PYI055: use Optional
    pass

