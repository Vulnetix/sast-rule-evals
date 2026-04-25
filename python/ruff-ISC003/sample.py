# Sample for Ruff rule ISC003: explicit-string-concatenation
# This file is designed to trigger the ISC003 rule.
# Run: ruff check --select ISC003 <this_file>

msg = (
    "hello "
    + "world"  # ISC003: use implicit concatenation
)

