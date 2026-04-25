# Sample for Ruff rule PT012: pytest-raises-with-multiple-statements
# This file is designed to trigger the PT012 rule.
# Run: ruff check --select PT012 <this_file>

import pytest


def test_foo():
    with pytest.raises(MyError):
        setup()
        func_to_test()  # not executed if `setup()` raises `MyError`
        assert foo()  # not executed
