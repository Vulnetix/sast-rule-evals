# Sample for Ruff rule SIM905: split-static-string
# This file is designed to trigger the SIM905 rule.
# Run: ruff check --select SIM905 <this_file>

"a,b,c,d".split(",")
