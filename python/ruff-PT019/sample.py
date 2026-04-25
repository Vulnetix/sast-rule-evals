# Sample for Ruff rule PT019: pytest-fixture-param-without-value
# This file is designed to trigger the PT019 rule.
# Run: ruff check --select PT019 <this_file>

import pytest


@pytest.fixture
def _patch_something(): ...


def test_foo(_patch_something): ...
