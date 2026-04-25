# Sample for Ruff rule FLY002: static-join-to-f-string
# This file is designed to trigger the FLY002 rule.
# Run: ruff check --select FLY002 <this_file>

" ".join((foo, bar))
