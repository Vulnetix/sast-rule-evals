# Sample for Ruff rule PLR2004: magic-value-comparison
# This file is designed to trigger the PLR2004 rule.
# Run: ruff check --select PLR2004 <this_file>

status = 200
if status == 200:  # PLR2004: magic value
    pass
if status == 404:
    pass

