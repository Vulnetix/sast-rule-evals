# Sample for Ruff rule PLW0120: useless-else-on-loop
# This file is designed to trigger the PLW0120 rule.
# Run: ruff check --select PLW0120 <this_file>

for item in items:
    print(item)
else:
    print("All items printed")
