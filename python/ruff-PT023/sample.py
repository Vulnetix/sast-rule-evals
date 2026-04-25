# Sample for Ruff rule PT023: pytest-incorrect-mark-parentheses-style
# This file is designed to trigger the PT023 rule.
# Run: ruff check --select PT023 <this_file>

import pytest

@pytest.mark.slow()  # PT023: no args needed
def test_slow():
    pass

