# Sample for Ruff rule PTH102: os-mkdir
# This file is designed to trigger the PTH102 rule.
# Run: ruff check --select PTH102 <this_file>

import os
os.mkdir("newdir")  # PTH102

