# Sample for Ruff rule FURB118: reimplemented-operator
# This file is designed to trigger the FURB118 rule.
# Run: ruff check --select FURB118 <this_file>

from functools import reduce
total = reduce(lambda x, y: x + y, numbers)  # FURB118: use operator.add

