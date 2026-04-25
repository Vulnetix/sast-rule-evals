# Sample for Ruff rule YTT301: sys-version0
# This file is designed to trigger the YTT301 rule.
# Run: ruff check --select YTT301 <this_file>

import sys

sys.version[0]  # If using Python 10, this evaluates to "1".
