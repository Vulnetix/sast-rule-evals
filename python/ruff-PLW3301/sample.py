# Sample for Ruff rule PLW3301: nested-min-max
# This file is designed to trigger the PLW3301 rule.
# Run: ruff check --select PLW3301 <this_file>

minimum = min(1, 2, min(3, 4, 5))
maximum = max(1, 2, max(3, 4, 5))
diff = maximum - minimum
