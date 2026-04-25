# Sample for Ruff rule PTH120: os-path-dirname
# This file is designed to trigger the PTH120 rule.
# Run: ruff check --select PTH120 <this_file>

import os
parent = os.path.dirname("/path/to/file.txt")  # PTH120

