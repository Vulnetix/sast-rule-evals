# Sample for Ruff rule PTH114: os-path-islink
# This file is designed to trigger the PTH114 rule.
# Run: ruff check --select PTH114 <this_file>

import os

os.path.islink("docs")
