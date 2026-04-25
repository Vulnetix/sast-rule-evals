# Sample for Ruff rule PT031: pytest-warns-with-multiple-statements
# This file is designed to trigger the PT031 rule.
# Run: ruff check --select PT031 <this_file>

import pytest


def test_foo_warns():
    with pytest.warns(Warning):
        setup()  # False negative if setup triggers a warning but foo does not.
        foo()
