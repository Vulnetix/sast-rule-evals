# Sample for Ruff rule PT013: pytest-incorrect-pytest-import
# This file is designed to trigger the PT013 rule.
# Run: ruff check --select PT013 <this_file>

import pytest as pt
from pytest import fixture
