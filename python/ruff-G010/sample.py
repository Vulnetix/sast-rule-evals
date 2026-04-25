# Sample for Ruff rule G010: logging-warn
# This file is designed to trigger the G010 rule.
# Run: ruff check --select G010 <this_file>

import logging
logging.warn("deprecated message")  # G010: use logging.warning

