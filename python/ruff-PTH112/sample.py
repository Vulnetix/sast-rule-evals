# Sample for Ruff rule PTH112: os-path-isdir
# This file is designed to trigger the PTH112 rule.
# Run: ruff check --select PTH112 <this_file>

import os
if os.path.isdir("mydir"):  # PTH112
    pass

