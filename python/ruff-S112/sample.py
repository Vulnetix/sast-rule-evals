# Sample for Ruff rule S112: try-except-continue
# This file is designed to trigger the S112 rule.
# Run: ruff check --select S112 <this_file>

import logging

while predicate:
    try:
        ...
    except Exception:
        continue
