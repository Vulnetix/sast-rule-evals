# Sample for Ruff rule C415: unnecessary-subscript-reversal
# This file is designed to trigger the C415 rule.
# Run: ruff check --select C415 <this_file>

sorted(iterable[::-1])
set(iterable[::-1])
reversed(iterable[::-1])
