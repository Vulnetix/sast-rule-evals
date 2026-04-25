# Sample for Ruff rule G002: logging-percent-format
# This file is designed to trigger the G002 rule.
# Run: ruff check --select G002 <this_file>

import logging
logging.info("User {} logged in".format(username))  # G002: .format()

