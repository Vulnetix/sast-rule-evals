# Sample for Ruff rule SIM300: yoda-conditions
# This file is designed to trigger the SIM300 rule.
# Run: ruff check --select SIM300 <this_file>

if None == x:  # SIM300: yoda condition
    pass

