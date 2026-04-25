# Sample for Ruff rule PTH108: os-unlink
# This file is designed to trigger the PTH108 rule.
# Run: ruff check --select PTH108 <this_file>

import os

os.unlink("file.py")
