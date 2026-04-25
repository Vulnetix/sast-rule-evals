# Sample for Ruff rule UP033: lru-cache-with-maxsize-none
# This file is designed to trigger the UP033 rule.
# Run: ruff check --select UP033 <this_file>

import functools


@functools.lru_cache(maxsize=None)
def foo(): ...
