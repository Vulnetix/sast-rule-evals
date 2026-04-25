# Sample for Ruff rule PLE1507: invalid-envvar-value
# This file is designed to trigger the PLE1507 rule.
# Run: ruff check --select PLE1507 <this_file>

import os
items = os.getenv("ITEMS", [])  # PLE1507: list default

