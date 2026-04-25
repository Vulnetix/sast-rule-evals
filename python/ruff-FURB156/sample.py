# Sample for Ruff rule FURB156: hardcoded-string-charset
# This file is designed to trigger the FURB156 rule.
# Run: ruff check --select FURB156 <this_file>

x = "0123456789"
y in "abcdefghijklmnopqrstuvwxyz"
