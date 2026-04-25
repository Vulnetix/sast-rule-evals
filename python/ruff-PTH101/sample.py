# Sample for Ruff rule PTH101: os-chmod
# This file is designed to trigger the PTH101 rule.
# Run: ruff check --select PTH101 <this_file>

import os
os.chmod("file.txt", 0o755)  # PTH101

