# Sample for Ruff rule PT025: pytest-erroneous-use-fixtures-on-fixture
# This file is designed to trigger the PT025 rule.
# Run: ruff check --select PT025 <this_file>

import pytest


@pytest.fixture()
def a():
    pass


@pytest.mark.usefixtures("a")
@pytest.fixture()
def b(a):
    pass
