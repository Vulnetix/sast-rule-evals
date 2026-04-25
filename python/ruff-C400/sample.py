# Sample for Ruff rule C400: unnecessary-generator-list
# This file is designed to trigger the C400 rule.
# Run: ruff check --select C400 <this_file>

list(f(x) for x in foo)
list(x for x in foo)
list((x for x in foo))
