# Sample for Ruff rule PLR1736: unnecessary-list-index-lookup
# This file is designed to trigger the PLR1736 rule.
# Run: ruff check --select PLR1736 <this_file>

letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(letters[index])
