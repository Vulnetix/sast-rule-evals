# Sample for Ruff rule B019: cached-instance-method
# This file is designed to trigger the B019 rule.
# Run: ruff check --select B019 <this_file>

from functools import lru_cache

class Cache:
    @lru_cache()
    def compute(self, x):  # B019: method lru_cache won't be GC'd
        return x * 2

