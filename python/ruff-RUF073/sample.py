# Sample for Ruff rule RUF073: f-string-percent-format
# This file is designed to trigger the RUF073 rule.
# Run: ruff check --select RUF073 <this_file>

f"{name}" % name
f"hello %s %s" % (first, second)
