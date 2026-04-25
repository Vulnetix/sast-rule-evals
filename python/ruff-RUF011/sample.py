# Sample for Ruff rule RUF011: ruff-static-key-dict-comprehension
# This file is designed to trigger the RUF011 rule.
# Run: ruff check --select RUF011 <this_file>

data = ["some", "Data"]
{"key": value.upper() for value in data}
