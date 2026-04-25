# Sample for Ruff rule FURB142: for-loop-set-mutations
# This file is designed to trigger the FURB142 rule.
# Run: ruff check --select FURB142 <this_file>

s = set()

for x in (1, 2, 3):
    s.add(x)

for x in (1, 2, 3):
    s.discard(x)
