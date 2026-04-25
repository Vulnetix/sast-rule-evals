# Sample for Ruff rule FURB161: bit-count
# This file is designed to trigger the FURB161 rule.
# Run: ruff check --select FURB161 <this_file>

x = bin(123).count("1")
y = bin(0b1111011).count("1")
