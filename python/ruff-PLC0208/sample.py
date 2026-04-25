# Sample for Ruff rule PLC0208: iteration-over-set
# This file is designed to trigger the PLC0208 rule.
# Run: ruff check --select PLC0208 <this_file>

for number in {1, 2, 3}:
    ...
