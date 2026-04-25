# Sample for Ruff rule FURB169: type-none-comparison
# This file is designed to trigger the FURB169 rule.
# Run: ruff check --select FURB169 <this_file>

type(obj) is type(None)
