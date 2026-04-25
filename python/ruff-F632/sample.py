# Sample for Ruff rule F632: is-literal
# This file is designed to trigger the F632 rule.
# Run: ruff check --select F632 <this_file>

x = 200
if x is 200:
    print("It's 200!")
