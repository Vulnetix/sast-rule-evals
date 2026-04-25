# Sample for Ruff rule PTH118: os-path-join
# This file is designed to trigger the PTH118 rule.
# Run: ruff check --select PTH118 <this_file>

import os
full = os.path.join("base", "file.txt")  # PTH118

