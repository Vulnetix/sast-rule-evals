# Sample for Ruff rule RUF034: useless-if-else
# This file is designed to trigger the RUF034 rule.
# Run: ruff check --select RUF034 <this_file>

foo = x if y else x
