# Sample for Ruff rule PTH106: os-rmdir
# This file is designed to trigger the PTH106 rule.
# Run: ruff check --select PTH106 <this_file>

import os

os.rmdir("folder/")
