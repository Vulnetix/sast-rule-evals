# Sample for Ruff rule PT021: pytest-fixture-finalizer-callback
# This file is designed to trigger the PT021 rule.
# Run: ruff check --select PT021 <this_file>

import pytest


@pytest.fixture()
def my_fixture(request):
    resource = acquire_resource()
    request.addfinalizer(resource.release)
    return resource
