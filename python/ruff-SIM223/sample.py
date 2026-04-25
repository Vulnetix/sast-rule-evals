# Sample for Ruff rule SIM223: expr-and-false
# This file is designed to trigger the SIM223 rule.
# Run: ruff check --select SIM223 <this_file>

if x and [] and y:
    pass

a = x and [] and y
