# Sample for Ruff rule RUF055: unnecessary-regular-expression
# This file is designed to trigger the RUF055 rule.
# Run: ruff check --select RUF055 <this_file>

re.sub("abc", "", s)
