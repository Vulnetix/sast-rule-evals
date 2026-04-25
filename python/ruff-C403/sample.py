# Sample for Ruff rule C403: unnecessary-list-comprehension-set
# This file is designed to trigger the C403 rule.
# Run: ruff check --select C403 <this_file>

set([f(x) for x in foo])
