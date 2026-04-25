# Sample for Ruff rule PT006: pytest-parametrize-names-wrong-type
# This file is designed to trigger the PT006 rule.
# Run: ruff check --select PT006 <this_file>

import pytest

@pytest.mark.parametrize("x,y", [(1, 2)])  # PT006
def test_add(x, y):
    assert x + y == 3

