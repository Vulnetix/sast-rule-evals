# Sample for Ruff rule YTT102: sys-version2
# This file is designed to trigger the YTT102 rule.
# Run: ruff check --select YTT102 <this_file>

import sys

sys.version[2]  # Evaluates to "1" on Python 3.10.
