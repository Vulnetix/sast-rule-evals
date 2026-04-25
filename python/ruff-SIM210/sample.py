# Sample for Ruff rule SIM210: if-expr-with-true-false
# This file is designed to trigger the SIM210 rule.
# Run: ruff check --select SIM210 <this_file>

flag = True if condition else False  # SIM210: use bool(condition)

