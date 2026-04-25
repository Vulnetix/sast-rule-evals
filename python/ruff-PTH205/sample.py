# Sample for Ruff rule PTH205: os-path-getctime
# This file is designed to trigger the PTH205 rule.
# Run: ruff check --select PTH205 <this_file>

import os

os.path.getctime(__file__)
