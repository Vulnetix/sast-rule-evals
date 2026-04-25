# Sample for Ruff rule C420: unnecessary-dict-comprehension-for-iterable
# This file is designed to trigger the C420 rule.
# Run: ruff check --select C420 <this_file>

{a: None for a in iterable}
{a: 1 for a in iterable}
