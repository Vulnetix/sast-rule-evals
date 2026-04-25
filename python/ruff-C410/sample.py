# Sample for Ruff rule C410: unnecessary-literal-within-list-call
# This file is designed to trigger the C410 rule.
# Run: ruff check --select C410 <this_file>

list([1, 2])
list((1, 2))
