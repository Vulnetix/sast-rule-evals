# Sample for Ruff rule PT017: pytest-assert-in-except
# This file is designed to trigger the PT017 rule.
# Run: ruff check --select PT017 <this_file>

def test_foo():
    try:
        1 / 0
    except ZeroDivisionError as e:
        assert e.args
