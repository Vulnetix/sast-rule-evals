# Sample for Ruff rule C401: unnecessary-generator-set
# This file is designed to trigger the C401 rule.
# Run: ruff check --select C401 <this_file>

set(f(x) for x in foo)
set(x for x in foo)
set((x for x in foo))
