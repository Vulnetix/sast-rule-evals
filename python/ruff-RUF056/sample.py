# Sample for Ruff rule RUF056: falsy-dict-get-fallback
# This file is designed to trigger the RUF056 rule.
# Run: ruff check --select RUF056 <this_file>

if dict.get(key, False):
    ...
