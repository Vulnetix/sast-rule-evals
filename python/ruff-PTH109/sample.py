# Sample for Ruff rule PTH109: os-getcwd
# This file is designed to trigger the PTH109 rule.
# Run: ruff check --select PTH109 <this_file>

import os
cwd = os.getcwd()  # PTH109

