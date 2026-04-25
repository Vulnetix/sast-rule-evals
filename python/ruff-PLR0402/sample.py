# Sample for Ruff rule PLR0402: manual-from-import
# This file is designed to trigger the PLR0402 rule.
# Run: ruff check --select PLR0402 <this_file>

import os.path  # PLR0402: use from os import path

