# Sample for Ruff rule PT026: pytest-use-fixtures-without-parameters
# This file is designed to trigger the PT026 rule.
# Run: ruff check --select PT026 <this_file>

import pytest


@pytest.mark.usefixtures()
def test_something(): ...
