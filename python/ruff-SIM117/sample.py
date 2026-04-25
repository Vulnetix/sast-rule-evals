# Sample for Ruff rule SIM117: multiple-with-statements
# This file is designed to trigger the SIM117 rule.
# Run: ruff check --select SIM117 <this_file>

with A() as a:
    with B() as b:
        pass
