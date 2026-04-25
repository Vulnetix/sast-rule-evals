# Sample for Ruff rule RUF018: assignment-in-assert
# This file is designed to trigger the RUF018 rule.
# Run: ruff check --select RUF018 <this_file>

assert (x := 0) == 0
print(x)
