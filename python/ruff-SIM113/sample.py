# Sample for Ruff rule SIM113: enumerate-for-loop
# This file is designed to trigger the SIM113 rule.
# Run: ruff check --select SIM113 <this_file>

fruits = ["apple", "banana", "cherry"]
i = 0
for fruit in fruits:
    print(f"{i + 1}. {fruit}")
    i += 1
