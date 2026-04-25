# Sample for Ruff rule SIM109: compare-with-tuple
# This file is designed to trigger the SIM109 rule.
# Run: ruff check --select SIM109 <this_file>

if x == 1 or x == 2 or x == 3:  # SIM109: use in
    pass

