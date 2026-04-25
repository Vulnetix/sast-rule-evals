# Sample for Ruff rule PLR6201: literal-membership
# This file is designed to trigger the PLR6201 rule.
# Run: ruff check --select PLR6201 <this_file>

if x in [1, 2, 3]:  # PLR6201: use set literal
    pass

