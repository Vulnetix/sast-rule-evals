# Sample for Ruff rule UP029: unnecessary-builtin-import
# This file is designed to trigger the UP029 rule.
# Run: ruff check --select UP029 <this_file>

from builtins import str

str(1)
