# Sample for Ruff rule SIM101: duplicate-isinstance-call
# This file is designed to trigger the SIM101 rule.
# Run: ruff check --select SIM101 <this_file>

def is_valid(x):
    return isinstance(x, int) or isinstance(x, float)  # SIM101: merge

