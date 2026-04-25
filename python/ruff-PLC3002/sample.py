# Sample for Ruff rule PLC3002: unnecessary-direct-lambda-call
# This file is designed to trigger the PLC3002 rule.
# Run: ruff check --select PLC3002 <this_file>

area = (lambda r: 3.14 * r**2)(radius)
