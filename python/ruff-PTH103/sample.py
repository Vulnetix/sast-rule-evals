# Sample for Ruff rule PTH103: os-makedirs
# This file is designed to trigger the PTH103 rule.
# Run: ruff check --select PTH103 <this_file>

import os

os.makedirs("./nested/directory/")
