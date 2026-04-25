# Sample for Ruff rule SIM911: zip-dict-keys-and-values
# This file is designed to trigger the SIM911 rule.
# Run: ruff check --select SIM911 <this_file>

flag_stars = {"USA": 50, "Slovenia": 3, "Panama": 2, "Australia": 6}

for country, stars in zip(flag_stars.keys(), flag_stars.values()):
    print(f"{country}'s flag has {stars} stars.")
