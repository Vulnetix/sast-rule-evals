# Sample for Ruff rule B030: except-with-non-exception-classes
# This file is designed to trigger the B030 rule.
# Run: ruff check --select B030 <this_file>

try:
    1 / 0
except 1:
    ...
