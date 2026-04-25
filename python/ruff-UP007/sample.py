# Sample for Ruff rule UP007: non-pep604-annotation-union
# This file is designed to trigger the UP007 rule.
# Run: ruff check --select UP007 <this_file>

from typing import Optional, Union

def foo(x: Optional[str]) -> Union[int, str]:  # UP007
    return x or 0

