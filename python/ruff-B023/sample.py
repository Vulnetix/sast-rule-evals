# Sample for Ruff rule B023: function-uses-loop-variable
# This file is designed to trigger the B023 rule.
# Run: ruff check --select B023 <this_file>

adders = [lambda x: x + i for i in range(3)]
values = [adder(1) for adder in adders]  # [3, 3, 3]
