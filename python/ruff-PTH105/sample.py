# Sample for Ruff rule PTH105: os-replace
# This file is designed to trigger the PTH105 rule.
# Run: ruff check --select PTH105 <this_file>

import os

os.replace("old.py", "new.py")
