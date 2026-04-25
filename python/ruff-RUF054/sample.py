# Sample for Ruff rule RUF054: indented-form-feed
# This file is designed to trigger the RUF054 rule.
# Run: ruff check --select RUF054 <this_file>

if foo():\n    \fbar()
