# Sample for Ruff rule RUF019: unnecessary-key-check
# This file is designed to trigger the RUF019 rule.
# Run: ruff check --select RUF019 <this_file>

d = {"key": "value"}
if "key" in d:
    val = d["key"]  # RUF019: unnecessary key check

