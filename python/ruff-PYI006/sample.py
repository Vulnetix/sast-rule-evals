# Sample for Ruff rule PYI006: bad-version-info-comparison
# This file is designed to trigger the PYI006 rule.
# Run: ruff check --select PYI006 <this_file>

import sys
if sys.version_info > (3, 9):  # PYI006: use >= for version check
    pass

