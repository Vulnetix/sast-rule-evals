# Sample for Ruff rule N813: camelcase-imported-as-lowercase
# This file is designed to trigger the N813 rule.
# Run: ruff check --select N813 <this_file>

from example import MyClassName as myclassname
