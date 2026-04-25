# Sample for Ruff rule C409: unnecessary-literal-within-tuple-call
# This file is designed to trigger the C409 rule.
# Run: ruff check --select C409 <this_file>

tuple([1, 2])
tuple((1, 2))
tuple([x for x in range(10)])
