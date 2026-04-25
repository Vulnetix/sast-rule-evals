# Sample for Ruff rule PT016: pytest-fail-without-message
# This file is designed to trigger the PT016 rule.
# Run: ruff check --select PT016 <this_file>

import pytest


def test_foo():
    pytest.fail()


def test_bar():
    pytest.fail("")


def test_baz():
    pytest.fail(reason="")
