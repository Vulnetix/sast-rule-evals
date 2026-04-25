# Sample for Ruff rule C404: unnecessary-list-comprehension-dict
# This file is designed to trigger the C404 rule.
# Run: ruff check --select C404 <this_file>

dict([(x, f(x)) for x in foo])
