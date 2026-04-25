# Sample for Ruff rule B909: loop-iterator-mutation
# This file is designed to trigger the B909 rule.
# Run: ruff check --select B909 <this_file>

items = [1, 2, 3]

for item in items:
    print(item)

    # Create an infinite loop by appending to the list.
    items.append(item)
