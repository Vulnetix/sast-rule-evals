# Sample for Ruff rule G001: logging-string-format
# This file is designed to trigger the G001 rule.
# Run: ruff check --select G001 <this_file>

import logging
logging.info("User %s logged in" % username)  # G001: %-format

