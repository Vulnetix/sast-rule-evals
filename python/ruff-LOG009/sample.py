# Sample for Ruff rule LOG009: undocumented-warn
# This file is designed to trigger the LOG009 rule.
# Run: ruff check --select LOG009 <this_file>

import logging
logging.WARN  # LOG009: deprecated

