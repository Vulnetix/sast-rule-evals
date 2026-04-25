# Sample for Ruff rule PTH121: os-path-samefile
# This file is designed to trigger the PTH121 rule.
# Run: ruff check --select PTH121 <this_file>

import os

os.path.samefile("f1.py", "f2.py")
