# Sample for Ruff rule C402: unnecessary-generator-dict
# This file is designed to trigger the C402 rule.
# Run: ruff check --select C402 <this_file>

dict((x, f(x)) for x in foo)
