# Sample for Ruff rule PTH122: os-path-splitext
# This file is designed to trigger the PTH122 rule.
# Run: ruff check --select PTH122 <this_file>

import os
base, ext = os.path.splitext("file.txt")  # PTH122

