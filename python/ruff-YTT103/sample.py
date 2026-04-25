# Sample for Ruff rule YTT103: sys-version-cmp-str3
# This file is designed to trigger the YTT103 rule.
# Run: ruff check --select YTT103 <this_file>

import sys
if sys.version == "3.11":  # YTT103: use sys.version_info
    pass

