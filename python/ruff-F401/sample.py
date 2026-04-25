# Sample for Ruff rule F401: unused-import
# This file is designed to trigger the F401 rule.
# Run: ruff check --select F401 <this_file>

import os  # F401: imported but unused
import sys
print(sys.argv)

