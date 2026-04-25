# Sample for Ruff rule PLR1722: sys-exit-alias
# This file is designed to trigger the PLR1722 rule.
# Run: ruff check --select PLR1722 <this_file>

import sys
sys.exit(0)  # PLR1722: use sys.exit() without arg

