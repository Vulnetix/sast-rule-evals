# Sample for Ruff rule B016: raise-literal
# This file is designed to trigger the B016 rule.
# Run: ruff check --select B016 <this_file>

raise NotImplemented()  # B016: should be NotImplementedError

