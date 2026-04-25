# Sample for Ruff rule PTH204: os-path-getmtime
# This file is designed to trigger the PTH204 rule.
# Run: ruff check --select PTH204 <this_file>

import os

os.path.getmtime(__file__)
