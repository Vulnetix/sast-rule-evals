# Sample for Ruff rule YTT203: sys-version-info1-cmp-int
# This file is designed to trigger the YTT203 rule.
# Run: ruff check --select YTT203 <this_file>

import sys

if sys.version_info[1] < 7:
    print("Python 3.6 or earlier.")  # This will be printed on Python 4.0.
