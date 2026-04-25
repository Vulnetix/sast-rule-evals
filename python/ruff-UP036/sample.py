# Sample for Ruff rule UP036: outdated-version-block
# This file is designed to trigger the UP036 rule.
# Run: ruff check --select UP036 <this_file>

import sys
if sys.version_info < (2, 7):  # UP036: python 2 check
    pass

