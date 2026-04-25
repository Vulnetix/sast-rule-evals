# Sample for Ruff rule RUF047: needless-else
# This file is designed to trigger the RUF047 rule.
# Run: ruff check --select RUF047 <this_file>

if foo:
    bar()
else:
    pass
