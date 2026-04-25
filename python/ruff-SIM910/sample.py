# Sample for Ruff rule SIM910: dict-get-with-none-default
# This file is designed to trigger the SIM910 rule.
# Run: ruff check --select SIM910 <this_file>

ages = {"Tom": 23, "Maria": 23, "Dog": 11}
age = ages.get("Cat", None)
