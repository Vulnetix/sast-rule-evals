# Sample for Ruff rule SIM118: in-dict-keys
# This file is designed to trigger the SIM118 rule.
# Run: ruff check --select SIM118 <this_file>

d = {"key": "value"}
if "key" in d.keys():  # SIM118: use 'key in d'
    pass

