# Sample for Ruff rule YTT204: sys-version-info-minor-cmp-int
# This file is designed to trigger the YTT204 rule.
# Run: ruff check --select YTT204 <this_file>

import sys

if sys.version_info.minor < 7:
    print("Python 3.6 or earlier.")  # This will be printed on Python 4.0.
