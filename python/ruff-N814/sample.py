# Sample for Ruff rule N814: camelcase-imported-as-constant
# This file is designed to trigger the N814 rule.
# Run: ruff check --select N814 <this_file>

from example import MyClassName as MY_CLASS_NAME
