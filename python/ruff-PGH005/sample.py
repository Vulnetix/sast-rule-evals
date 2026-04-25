# Sample for Ruff rule PGH005: invalid-mock-access
# This file is designed to trigger the PGH005 rule.
# Run: ruff check --select PGH005 <this_file>

my_mock.assert_called
