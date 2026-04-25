# Sample for Ruff rule PYI017: complex-assignment-in-stub
# This file is designed to trigger the PYI017 rule.
# Run: ruff check --select PYI017 <this_file>

from typing import Union
def foo(x: Union[Union[int, str], float]) -> None:  # PYI017: nested Union
    pass

