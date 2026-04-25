# Sample for Ruff rule PT004: pytest-missing-fixture-name-underscore
# This file is designed to trigger the PT004 rule.
# Run: ruff check --select PT004 <this_file>

import pytest


@pytest.fixture()
def patch_something(mocker):
    mocker.patch("module.object")


@pytest.fixture()
def use_context():
    with create_context():
        yield
