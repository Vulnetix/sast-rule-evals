# Sample for Ruff rule SIM114: if-with-same-arms
# This file is designed to trigger the SIM114 rule.
# Run: ruff check --select SIM114 <this_file>

if x == 1:
    print("Hello")
elif x == 2:
    print("Hello")
