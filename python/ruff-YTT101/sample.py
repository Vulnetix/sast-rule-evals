# Sample for Ruff rule YTT101: sys-version-slice3
# This file is designed to trigger the YTT101 rule.
# Run: ruff check --select YTT101 <this_file>

import sys
ver = sys.version[:3]  # YTT101: use sys.version_info

