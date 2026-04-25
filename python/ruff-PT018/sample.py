# Sample for Ruff rule PT018: pytest-composite-assertion
# This file is designed to trigger the PT018 rule.
# Run: ruff check --select PT018 <this_file>

def test_valid(data):
    assert data and len(data) > 0  # PT018: composite assertion

