# Sample for Ruff rule SIM108: if-else-block-instead-of-if-exp
# This file is designed to trigger the SIM108 rule.
# Run: ruff check --select SIM108 <this_file>

if foo:
    bar = x
else:
    bar = y
