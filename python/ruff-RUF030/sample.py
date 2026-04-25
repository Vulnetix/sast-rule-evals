# Sample for Ruff rule RUF030: assert-with-print-message
# This file is designed to trigger the RUF030 rule.
# Run: ruff check --select RUF030 <this_file>

assert False, print("This is a message")
