# Sample for Ruff rule PT008: pytest-patch-with-lambda
# This file is designed to trigger the PT008 rule.
# Run: ruff check --select PT008 <this_file>

def test_foo(mocker):
    mocker.patch("module.target", lambda x, y: 7)
