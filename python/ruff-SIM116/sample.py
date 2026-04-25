# Sample for Ruff rule SIM116: if-else-block-instead-of-dict-lookup
# This file is designed to trigger the SIM116 rule.
# Run: ruff check --select SIM116 <this_file>

def describe(code):
    if code == "A":
        return "Alpha"
    elif code == "B":  # SIM116: use dict
        return "Beta"
    elif code == "C":
        return "Charlie"

