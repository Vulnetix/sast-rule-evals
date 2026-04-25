# Sample for Ruff rule PLW0128: redeclared-assigned-name
# This file is designed to trigger the PLW0128 rule.
# Run: ruff check --select PLW0128 <this_file>

a, b, a = (1, 2, 3)
print(a)  # 3
