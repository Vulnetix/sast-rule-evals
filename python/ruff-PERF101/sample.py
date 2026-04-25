# Sample for Ruff rule PERF101: unnecessary-list-cast
# This file is designed to trigger the PERF101 rule.
# Run: ruff check --select PERF101 <this_file>

items = [1, 2, 3]
for item in list(items):  # PERF101: unnecessary list cast
    print(item)

