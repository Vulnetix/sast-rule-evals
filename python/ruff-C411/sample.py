# Sample for Ruff rule C411: unnecessary-list-call
# This file is designed to trigger the C411 rule.
# Run: ruff check --select C411 <this_file>

list([f(x) for x in foo])
