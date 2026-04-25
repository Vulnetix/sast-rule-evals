# Sample for Ruff rule B911: batched-without-explicit-strict
# This file is designed to trigger the B911 rule.
# Run: ruff check --select B911 <this_file>

import itertools

itertools.batched(iterable, n)
