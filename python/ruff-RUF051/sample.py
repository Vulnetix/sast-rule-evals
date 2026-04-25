# Sample for Ruff rule RUF051: if-key-in-dict-del
# This file is designed to trigger the RUF051 rule.
# Run: ruff check --select RUF051 <this_file>

if key in dictionary:
    del dictionary[key]
