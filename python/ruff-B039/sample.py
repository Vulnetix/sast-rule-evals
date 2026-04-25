# Sample for Ruff rule B039: mutable-contextvar-default
# This file is designed to trigger the B039 rule.
# Run: ruff check --select B039 <this_file>

from contextvars import ContextVar


cv: ContextVar[list] = ContextVar("cv", default=[])
