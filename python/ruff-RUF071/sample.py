# Sample for Ruff rule RUF071: os-path-commonprefix
# This file is designed to trigger the RUF071 rule.
# Run: ruff check --select RUF071 <this_file>

import os

# Returns "/usr/l" — not a valid directory!
os.path.commonprefix(["/usr/lib", "/usr/local/lib"])
