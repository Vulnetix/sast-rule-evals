# Sample for Ruff rule SIM401: if-else-block-instead-of-dict-get
# This file is designed to trigger the SIM401 rule.
# Run: ruff check --select SIM401 <this_file>

foo = {}
if "bar" in foo:
    value = foo["bar"]
else:
    value = 0
