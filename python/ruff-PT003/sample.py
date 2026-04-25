# Sample for Ruff rule PT003: pytest-extraneous-scope-function
# This file is designed to trigger the PT003 rule.
# Run: ruff check --select PT003 <this_file>

import pytest

@pytest.fixture(scope="function")  # PT003: scope=function is default
def my_fixture():
    return 42

