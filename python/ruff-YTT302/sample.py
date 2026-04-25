# Sample for Ruff rule YTT302: sys-version-cmp-str10
# This file is designed to trigger the YTT302 rule.
# Run: ruff check --select YTT302 <this_file>

import sys

sys.version >= "3"  # `False` on Python 10.
