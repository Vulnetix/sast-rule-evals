# Sample for Ruff rule B007: unused-loop-control-variable
# This file is designed to trigger the B007 rule.
# Run: ruff check --select B007 <this_file>

for _idx in range(10):  # B007: unused loop var
    print("hello")

