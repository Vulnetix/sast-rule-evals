# Sample for Ruff rule RUF037: unnecessary-empty-iterable-within-deque-call
# This file is designed to trigger the RUF037 rule.
# Run: ruff check --select RUF037 <this_file>

from collections import deque

queue = deque(set())
queue = deque([], 10)
