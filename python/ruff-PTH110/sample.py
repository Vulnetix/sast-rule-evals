# Sample for Ruff rule PTH110: os-path-exists
# This file is designed to trigger the PTH110 rule.
# Run: ruff check --select PTH110 <this_file>

import os
if os.path.exists("file.txt"):  # PTH110
    pass

