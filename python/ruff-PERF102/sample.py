# Sample for Ruff rule PERF102: incorrect-dict-iterator
# This file is designed to trigger the PERF102 rule.
# Run: ruff check --select PERF102 <this_file>

obj = {"a": 1, "b": 2}
for key, value in obj.items():
    print(value)
