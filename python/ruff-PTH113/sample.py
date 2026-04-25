# Sample for Ruff rule PTH113: os-path-isfile
# This file is designed to trigger the PTH113 rule.
# Run: ruff check --select PTH113 <this_file>

import os
if os.path.isfile("file.txt"):  # PTH113
    pass

