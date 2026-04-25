# Sample for Ruff rule PTH207: glob
# This file is designed to trigger the PTH207 rule.
# Run: ruff check --select PTH207 <this_file>

import glob
import os

glob.glob(os.path.join("my_path", "requirements*.txt"))
