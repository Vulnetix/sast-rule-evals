# Sample for Ruff rule PTH104: os-rename
# This file is designed to trigger the PTH104 rule.
# Run: ruff check --select PTH104 <this_file>

import os

os.rename("old.py", "new.py")
