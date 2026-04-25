# Sample for Ruff rule SIM201: negate-equal-op
# This file is designed to trigger the SIM201 rule.
# Run: ruff check --select SIM201 <this_file>

x = 5
if not x == 10:  # SIM201: use !=
    pass

