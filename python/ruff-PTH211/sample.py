# Sample for Ruff rule PTH211: os-symlink
# This file is designed to trigger the PTH211 rule.
# Run: ruff check --select PTH211 <this_file>

import os

os.symlink("usr/bin/python", "tmp/python", target_is_directory=False)
