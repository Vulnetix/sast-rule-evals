# Sample for Ruff rule FURB148: unnecessary-enumerate
# This file is designed to trigger the FURB148 rule.
# Run: ruff check --select FURB148 <this_file>

for i, val in enumerate(items):
    if i == 0:  # FURB148: use zip/values instead
        pass

