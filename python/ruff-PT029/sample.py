# Sample for Ruff rule PT029: pytest-warns-without-warning
# This file is designed to trigger the PT029 rule.
# Run: ruff check --select PT029 <this_file>

import pytest


def test_foo():
    with pytest.warns():
        do_something()
