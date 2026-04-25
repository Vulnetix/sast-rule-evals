# Sample for Ruff rule PIE800: unnecessary-spread
# This file is designed to trigger the PIE800 rule.
# Run: ruff check --select PIE800 <this_file>

foo = {"A": 1, "B": 2}
bar = {**foo, **{"C": 3}}
