# Sample for Ruff rule C418: unnecessary-literal-within-dict-call
# This file is designed to trigger the C418 rule.
# Run: ruff check --select C418 <this_file>

dict({})
dict({"a": 1})
