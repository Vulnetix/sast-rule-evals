# Sample for Ruff rule RUF010: explicit-f-string-type-conversion
# This file is designed to trigger the RUF010 rule.
# Run: ruff check --select RUF010 <this_file>

value = 42
s = str(value)  # RUF010: use !s conversion

