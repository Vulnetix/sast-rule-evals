# Sample for Ruff rule ISC001: single-line-implicit-string-concatenation
# This file is designed to trigger the ISC001 rule.
# Run: ruff check --select ISC001 <this_file>

msg = "hello" "world"  # ISC001: implicit concat

