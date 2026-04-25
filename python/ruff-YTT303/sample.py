# Sample for Ruff rule YTT303: sys-version-slice1
# This file is designed to trigger the YTT303 rule.
# Run: ruff check --select YTT303 <this_file>

import sys

sys.version[:1]  # If using Python 10, this evaluates to "1".
