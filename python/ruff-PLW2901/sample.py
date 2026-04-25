# Sample for Ruff rule PLW2901: redefined-loop-name
# This file is designed to trigger the PLW2901 rule.
# Run: ruff check --select PLW2901 <this_file>

for item in items:
    item = item.strip()  # PLW2901: loop variable overwritten
    process(item)

