# Sample for Ruff rule PTH119: os-path-basename
# This file is designed to trigger the PTH119 rule.
# Run: ruff check --select PTH119 <this_file>

import os
name = os.path.basename("/path/to/file.txt")  # PTH119

