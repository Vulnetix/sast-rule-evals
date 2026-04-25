# Sample for Ruff rule PTH202: os-path-getsize
# This file is designed to trigger the PTH202 rule.
# Run: ruff check --select PTH202 <this_file>

import os

os.path.getsize(__file__)
