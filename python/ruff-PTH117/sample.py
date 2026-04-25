# Sample for Ruff rule PTH117: os-path-isabs
# This file is designed to trigger the PTH117 rule.
# Run: ruff check --select PTH117 <this_file>

import os

if os.path.isabs(file_name):
    print("Absolute path!")
