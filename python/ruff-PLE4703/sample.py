# Sample for Ruff rule PLE4703: modified-iterating-set
# This file is designed to trigger the PLE4703 rule.
# Run: ruff check --select PLE4703 <this_file>

nums = {1, 2, 3}
for num in nums:
    nums.add(num + 5)
