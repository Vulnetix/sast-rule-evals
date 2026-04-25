# Sample for Ruff rule PERF402: manual-list-copy
# This file is designed to trigger the PERF402 rule.
# Run: ruff check --select PERF402 <this_file>

original = [1, 2, 3]
copy = []
for item in original:
    copy.append(item)  # PERF402: use list() or copy()

