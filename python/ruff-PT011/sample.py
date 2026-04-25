# Sample for Ruff rule PT011: pytest-raises-too-broad
# This file is designed to trigger the PT011 rule.
# Run: ruff check --select PT011 <this_file>

import pytest

def test_raises():
    with pytest.raises(Exception):  # PT011: too broad
        do_something()

