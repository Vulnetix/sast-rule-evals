# Sample for Ruff rule PERF203: try-except-in-loop
# This file is designed to trigger the PERF203 rule.
# Run: ruff check --select PERF203 <this_file>

items = [1, 2, 3]
for item in items:
    try:
        results.append(process(item))  # PERF203: try in loop
    except ValueError:
        pass

