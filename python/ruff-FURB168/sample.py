# Sample for Ruff rule FURB168: isinstance-type-none
# This file is designed to trigger the FURB168 rule.
# Run: ruff check --select FURB168 <this_file>

isinstance(obj, type(None))
