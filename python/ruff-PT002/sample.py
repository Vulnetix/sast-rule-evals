# Sample for Ruff rule PT002: pytest-fixture-positional-args
# This file is designed to trigger the PT002 rule.
# Run: ruff check --select PT002 <this_file>

import pytest


@pytest.fixture("module")
def my_fixture(): ...
