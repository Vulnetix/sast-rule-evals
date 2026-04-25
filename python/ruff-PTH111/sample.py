# Sample for Ruff rule PTH111: os-path-expanduser
# This file is designed to trigger the PTH111 rule.
# Run: ruff check --select PTH111 <this_file>

import os

os.path.expanduser("~/films/Monty Python")
