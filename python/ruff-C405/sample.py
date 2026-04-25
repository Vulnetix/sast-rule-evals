# Sample for Ruff rule C405: unnecessary-literal-set
# This file is designed to trigger the C405 rule.
# Run: ruff check --select C405 <this_file>

set([1, 2])
set((1, 2))
set([])
