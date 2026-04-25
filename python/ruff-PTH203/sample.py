# Sample for Ruff rule PTH203: os-path-getatime
# This file is designed to trigger the PTH203 rule.
# Run: ruff check --select PTH203 <this_file>

import os

os.path.getatime(__file__)
