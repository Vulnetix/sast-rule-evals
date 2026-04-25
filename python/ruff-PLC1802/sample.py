# Sample for Ruff rule PLC1802: len-test
# This file is designed to trigger the PLC1802 rule.
# Run: ruff check --select PLC1802 <this_file>

fruits = ["orange", "apple"]
vegetables = []

if len(fruits):
    print(fruits)

if not len(vegetables):
    print(vegetables)
