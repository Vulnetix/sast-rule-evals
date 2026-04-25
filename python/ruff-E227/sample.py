# Sample for Ruff rule E227: missing-whitespace-around-bitwise-or-shift-operator
# This file is designed to trigger the E227 rule.
# Run: ruff check --select E227 <this_file>

x = 128<<1
