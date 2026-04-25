# Sample for Ruff rule PLE1141: dict-iter-missing-items
# This file is designed to trigger the PLE1141 rule.
# Run: ruff check --select PLE1141 <this_file>

data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}

for city, population in data:
    print(f"{city} has population {population}.")
