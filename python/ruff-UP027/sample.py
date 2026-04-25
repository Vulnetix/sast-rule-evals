# Sample for Ruff rule UP027: unpacked-list-comprehension
# This file is designed to trigger the UP027 rule.
# Run: ruff check --select UP027 <this_file>

a, b, c = [foo(x) for x in items]
