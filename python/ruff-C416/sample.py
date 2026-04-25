# Sample for Ruff rule C416: unnecessary-comprehension
# This file is designed to trigger the C416 rule.
# Run: ruff check --select C416 <this_file>

{a: b for a, b in iterable}
[x for x in iterable]
{x for x in iterable}
