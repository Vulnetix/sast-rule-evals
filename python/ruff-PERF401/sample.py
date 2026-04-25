# Sample for Ruff rule PERF401: manual-list-comprehension
# This file is designed to trigger the PERF401 rule.
# Run: ruff check --select PERF401 <this_file>

items = [1, 2, 3]
result = []
for item in items:
    result.append(item * 2)  # PERF401: use list comprehension

