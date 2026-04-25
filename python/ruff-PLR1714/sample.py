# Sample for Ruff rule PLR1714: repeated-equality-comparison
# This file is designed to trigger the PLR1714 rule.
# Run: ruff check --select PLR1714 <this_file>

if x != "a" and x != "b":  # PLR1714: use not in
    pass

