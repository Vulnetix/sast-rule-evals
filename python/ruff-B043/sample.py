# Sample for Ruff rule B043: del-attr-with-constant
# This file is designed to trigger the B043 rule.
# Run: ruff check --select B043 <this_file>

delattr(obj, "foo")
