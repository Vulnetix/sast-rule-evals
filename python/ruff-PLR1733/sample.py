# Sample for Ruff rule PLR1733: unnecessary-dict-index-lookup
# This file is designed to trigger the PLR1733 rule.
# Run: ruff check --select PLR1733 <this_file>

FRUITS = {"apple": 1, "orange": 10, "berry": 22}

for fruit_name, fruit_count in FRUITS.items():
    print(FRUITS[fruit_name])
