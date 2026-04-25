# Sample for Ruff rule C406: unnecessary-literal-dict
# This file is designed to trigger the C406 rule.
# Run: ruff check --select C406 <this_file>

dict([(1, 2), (3, 4)])
dict(((1, 2), (3, 4)))
dict([])
