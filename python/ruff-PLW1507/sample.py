# Sample for Ruff rule PLW1507: shallow-copy-environ
# This file is designed to trigger the PLW1507 rule.
# Run: ruff check --select PLW1507 <this_file>

import copy
import os

env = copy.copy(os.environ)
