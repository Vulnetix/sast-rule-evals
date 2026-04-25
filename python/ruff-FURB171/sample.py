# Sample for Ruff rule FURB171: single-item-membership-test
# This file is designed to trigger the FURB171 rule.
# Run: ruff check --select FURB171 <this_file>

if x in [1]:  # FURB171: use (1,) or just == 1
    pass

