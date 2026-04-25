# Sample for Ruff rule B026: star-arg-unpacking-after-keyword-arg
# This file is designed to trigger the B026 rule.
# Run: ruff check --select B026 <this_file>

def foo(*args, key="default"):  # B026: star before keyword
    pass

