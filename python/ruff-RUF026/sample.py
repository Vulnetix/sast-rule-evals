# Sample for Ruff rule RUF026: default-factory-kwarg
# This file is designed to trigger the RUF026 rule.
# Run: ruff check --select RUF026 <this_file>

defaultdict(default_factory=int)
defaultdict(default_factory=list)
