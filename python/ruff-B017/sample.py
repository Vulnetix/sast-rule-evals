# Sample for Ruff rule B017: assert-raises-exception
# This file is designed to trigger the B017 rule.
# Run: ruff check --select B017 <this_file>

import pytest

def test_something():
    with pytest.raises(Exception):  # B017: too broad
        risky_operation()

