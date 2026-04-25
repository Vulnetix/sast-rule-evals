# Sample for Ruff rule ANN401: any-type
# This file is designed to trigger the ANN401 rule.
# Run: ruff check --select ANN401 <this_file>

from typing import Any


def foo(x: Any): ...
