# Sample for Ruff rule RUF024: mutable-fromkeys-value
# This file is designed to trigger the RUF024 rule.
# Run: ruff check --select RUF024 <this_file>

cities = dict.fromkeys(["UK", "Poland"], [])
cities["UK"].append("London")
cities["Poland"].append("Poznan")
print(cities)  # {'UK': ['London', 'Poznan'], 'Poland': ['London', 'Poznan']}
