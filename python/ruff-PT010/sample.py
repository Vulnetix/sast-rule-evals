# Sample for Ruff rule PT010: pytest-raises-without-exception
# This file is designed to trigger the PT010 rule.
# Run: ruff check --select PT010 <this_file>

import pytest


def test_foo():
    with pytest.raises():
        do_something()
