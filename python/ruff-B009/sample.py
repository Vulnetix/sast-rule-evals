# Sample for Ruff rule B009: get-attr-with-constant
# This file is designed to trigger the B009 rule.
# Run: ruff check --select B009 <this_file>

obj = getattr(target, "name")  # B009: constant attr

