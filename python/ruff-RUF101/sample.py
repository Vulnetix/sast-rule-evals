# Sample for Ruff rule RUF101: redirected-noqa
# This file is designed to trigger the RUF101 rule.
# Run: ruff check --select RUF101 <this_file>

x = eval(command)  # noqa: PGH001
