# Sample for Ruff rule B035: static-key-dict-comprehension
# This file is designed to trigger the B035 rule.
# Run: ruff check --select B035 <this_file>

{key: value for key in ["fixed_key"]}  # B035: static key in dict comp

