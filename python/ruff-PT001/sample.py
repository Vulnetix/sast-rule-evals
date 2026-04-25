# Sample for Ruff rule PT001: pytest-fixture-incorrect-parentheses-style
# This file is designed to trigger the PT001 rule.
# Run: ruff check --select PT001 <this_file>

import pytest

@pytest.fixture()  # PT001: unnecessary parens
def my_fixture():
    return 42

