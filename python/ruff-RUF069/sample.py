# Sample for Ruff rule RUF069: float-equality-comparison
# This file is designed to trigger the RUF069 rule.
# Run: ruff check --select RUF069 <this_file>

assert 0.1 + 0.2 == 0.3  # AssertionError

assert complex(0.3, 0.1) == complex(0.1 + 0.2, 0.1)  # AssertionError
