# Sample for Ruff rule PT015: pytest-assert-always-false
# This file is designed to trigger the PT015 rule.
# Run: ruff check --select PT015 <this_file>

def test_always_fails():
    assert False, "This always fails"  # PT015: use pytest.fail()

