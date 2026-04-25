# Sample for Ruff rule RUF050: unnecessary-if
# This file is designed to trigger the RUF050 rule.
# Run: ruff check --select RUF050 <this_file>

import sys

if sys.version_info >= (3, 11):
    pass
