# Sample for Ruff rule RUF046: unnecessary-cast-to-int
# This file is designed to trigger the RUF046 rule.
# Run: ruff check --select RUF046 <this_file>

int(len([]))
int(round(foo, None))
