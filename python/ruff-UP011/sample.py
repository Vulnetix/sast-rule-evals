# Sample for Ruff rule UP011: lru-cache-without-parameters
# This file is designed to trigger the UP011 rule.
# Run: ruff check --select UP011 <this_file>

from functools import lru_cache

@lru_cache()  # UP011: use @lru_cache without ()
def expensive(n):
    return n * 2

