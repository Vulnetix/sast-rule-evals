# Sample for Ruff rule E402: module-import-not-at-top-of-file
# This file is designed to trigger the E402 rule.
# Run: ruff check --select E402 <this_file>

"One string"
"Two string"
a = 1
import os
from sys import x
