# Sample for Ruff rule B011: assert-false
# This file is designed to trigger the B011 rule.
# Run: ruff check --select B011 <this_file>

assert False, "Should not reach here"  # B011

