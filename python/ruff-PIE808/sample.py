# Sample for Ruff rule PIE808: unnecessary-range-start
# This file is designed to trigger the PIE808 rule.
# Run: ruff check --select PIE808 <this_file>

for i in range(0, 10):  # PIE808: unnecessary start=0
    print(i)

