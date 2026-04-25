# Sample for Ruff rule PTH115: os-readlink
# This file is designed to trigger the PTH115 rule.
# Run: ruff check --select PTH115 <this_file>

import os

os.readlink(file_name)
