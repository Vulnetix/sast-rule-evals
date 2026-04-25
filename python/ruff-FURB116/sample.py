# Sample for Ruff rule FURB116: f-string-number-format
# This file is designed to trigger the FURB116 rule.
# Run: ruff check --select FURB116 <this_file>

print(bin(1337)[2:])
