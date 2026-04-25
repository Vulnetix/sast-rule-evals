# Sample for Ruff rule PT020: pytest-deprecated-yield-fixture
# This file is designed to trigger the PT020 rule.
# Run: ruff check --select PT020 <this_file>

import pytest


@pytest.yield_fixture()
def my_fixture():
    obj = SomeClass()
    yield obj
    obj.cleanup()
