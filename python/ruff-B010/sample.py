# Sample for Ruff rule B010: set-attr-with-constant
# This file is designed to trigger the B010 rule.
# Run: ruff check --select B010 <this_file>

setattr(target, "name", "value")  # B010: constant attr

