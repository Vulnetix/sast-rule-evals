# Sample for Ruff rule SIM211: if-expr-with-false-true
# This file is designed to trigger the SIM211 rule.
# Run: ruff check --select SIM211 <this_file>

flag = False if condition else True  # SIM211: use not condition

