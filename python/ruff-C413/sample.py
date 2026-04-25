# Sample for Ruff rule C413: unnecessary-call-around-sorted
# This file is designed to trigger the C413 rule.
# Run: ruff check --select C413 <this_file>

reversed(sorted(iterable))
