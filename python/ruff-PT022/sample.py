# Sample for Ruff rule PT022: pytest-useless-yield-fixture
# This file is designed to trigger the PT022 rule.
# Run: ruff check --select PT022 <this_file>

import pytest


@pytest.fixture()
def my_fixture():
    resource = acquire_resource()
    yield resource
