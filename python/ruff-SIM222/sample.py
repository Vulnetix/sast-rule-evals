# Sample for Ruff rule SIM222: expr-or-true
# This file is designed to trigger the SIM222 rule.
# Run: ruff check --select SIM222 <this_file>

if x or [1] or y:
    pass

a = x or [1] or y
