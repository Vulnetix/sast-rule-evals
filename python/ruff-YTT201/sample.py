# Sample for Ruff rule YTT201: sys-version-info0-eq3
# This file is designed to trigger the YTT201 rule.
# Run: ruff check --select YTT201 <this_file>

import sys
if sys.version_info[0] == 3:  # YTT201: always True
    pass

