# Sample for Ruff rule PT024: pytest-unnecessary-asyncio-mark-on-fixture
# This file is designed to trigger the PT024 rule.
# Run: ruff check --select PT024 <this_file>

import pytest


@pytest.mark.asyncio()
@pytest.fixture()
async def my_fixture():
    return 0
