# Sample for Ruff rule PT005: pytest-incorrect-fixture-name-underscore
# This file is designed to trigger the PT005 rule.
# Run: ruff check --select PT005 <this_file>

import pytest


@pytest.fixture()
def _some_object():
    return SomeClass()


@pytest.fixture()
def _some_object_with_cleanup():
    obj = SomeClass()
    yield obj
    obj.cleanup()
