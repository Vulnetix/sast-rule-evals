# Sample for Ruff rule C417: unnecessary-map
# This file is designed to trigger the C417 rule.
# Run: ruff check --select C417 <this_file>

map(lambda x: x + 1, iterable)
