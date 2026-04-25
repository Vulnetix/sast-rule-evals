# Sample for Ruff rule PT030: pytest-warns-too-broad
# This file is designed to trigger the PT030 rule.
# Run: ruff check --select PT030 <this_file>

import pytest


def test_foo():
    with pytest.warns(Warning):
        ...

    # empty string is also an error
    with pytest.warns(Warning, match=""):
        ...
