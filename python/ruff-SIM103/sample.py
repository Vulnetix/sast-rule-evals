# Sample for Ruff rule SIM103: needless-bool
# This file is designed to trigger the SIM103 rule.
# Run: ruff check --select SIM103 <this_file>

def is_valid(x):
    if x > 0:
        return True  # SIM103: return condition directly
    else:
        return False

