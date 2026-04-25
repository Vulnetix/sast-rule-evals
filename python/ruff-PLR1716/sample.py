# Sample for Ruff rule PLR1716: boolean-chained-comparison
# This file is designed to trigger the PLR1716 rule.
# Run: ruff check --select PLR1716 <this_file>

a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    pass
