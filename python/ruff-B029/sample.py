# Sample for Ruff rule B029: except-with-empty-tuple
# This file is designed to trigger the B029 rule.
# Run: ruff check --select B029 <this_file>

try:
    pass
except ():  # B029: empty exception tuple
    pass

