# Sample for Ruff rule PERF403: manual-dict-comprehension
# This file is designed to trigger the PERF403 rule.
# Run: ruff check --select PERF403 <this_file>

pairs = (("a", 1), ("b", 2))
result = {}
for x, y in pairs:
    if y % 2:
        result[x] = y
