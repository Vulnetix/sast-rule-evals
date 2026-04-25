# Sample for Ruff rule PT007: pytest-parametrize-values-wrong-type
# This file is designed to trigger the PT007 rule.
# Run: ruff check --select PT007 <this_file>

import pytest


# expected list, got tuple
@pytest.mark.parametrize("param", (1, 2))
def test_foo(param): ...


# expected top-level list, got tuple
@pytest.mark.parametrize(
    ("param1", "param2"),
    (
        (1, 2),
        (3, 4),
    ),
)
def test_bar(param1, param2): ...


# expected individual rows to be tuples, got lists
@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        [1, 2],
        [3, 4],
    ],
)
def test_baz(param1, param2): ...
