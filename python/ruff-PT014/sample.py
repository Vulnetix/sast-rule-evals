# Sample for Ruff rule PT014: pytest-duplicate-parametrize-test-cases
# This file is designed to trigger the PT014 rule.
# Run: ruff check --select PT014 <this_file>

import pytest


@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (1, 2),
        (1, 2),
    ],
)
def test_foo(param1, param2): ...
