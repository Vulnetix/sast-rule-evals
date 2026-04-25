# Sample for Ruff rule ISC002: multi-line-implicit-string-concatenation
# This file is designed to trigger the ISC002 rule.
# Run: ruff check --select ISC002 <this_file>

msg = ("hello "
       "world")  # ISC002: implicit multiline concat

