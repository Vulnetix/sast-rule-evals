# Sample for Ruff rule RUF016: invalid-index-type
# This file is designed to trigger the RUF016 rule.
# Run: ruff check --select RUF016 <this_file>

var = [1, 2, 3]["x"]
