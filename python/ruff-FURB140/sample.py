# Sample for Ruff rule FURB140: reimplemented-starmap
# This file is designed to trigger the FURB140 rule.
# Run: ruff check --select FURB140 <this_file>

all(predicate(a, b) for a, b in some_iterable)
