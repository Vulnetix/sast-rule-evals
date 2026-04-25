# Sample for Ruff rule PTH100: os-path-abspath
# This file is designed to trigger the PTH100 rule.
# Run: ruff check --select PTH100 <this_file>

import os
path = os.path.abspath("file.txt")  # PTH100

