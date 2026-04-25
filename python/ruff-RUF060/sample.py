# Sample for Ruff rule RUF060: in-empty-collection
# This file is designed to trigger the RUF060 rule.
# Run: ruff check --select RUF060 <this_file>

if 1 not in set():
    print("got it!")
