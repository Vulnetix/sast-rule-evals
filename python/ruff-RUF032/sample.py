# Sample for Ruff rule RUF032: decimal-from-float-literal
# This file is designed to trigger the RUF032 rule.
# Run: ruff check --select RUF032 <this_file>

num = Decimal(1.2345)
