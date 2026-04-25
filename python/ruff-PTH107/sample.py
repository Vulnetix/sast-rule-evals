# Sample for Ruff rule PTH107: os-remove
# This file is designed to trigger the PTH107 rule.
# Run: ruff check --select PTH107 <this_file>

import os
os.remove("file.txt")  # PTH107

