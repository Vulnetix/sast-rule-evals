# Sample for Ruff rule ARG005: unused-lambda-argument
# This file is designed to trigger the ARG005 rule.
# Run: ruff check --select ARG005 <this_file>

my_list = [1, 2, 3, 4, 5]
squares = map(lambda x, y: x**2, my_list)
