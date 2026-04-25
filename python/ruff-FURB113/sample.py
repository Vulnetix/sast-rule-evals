# Sample for Ruff rule FURB113: repeated-append
# This file is designed to trigger the FURB113 rule.
# Run: ruff check --select FURB113 <this_file>

results = []
for item in items:
    results.append(item.strip())  # FURB113: use list.extend()

