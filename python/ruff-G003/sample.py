# Sample for Ruff rule G003: logging-string-concat
# This file is designed to trigger the G003 rule.
# Run: ruff check --select G003 <this_file>

import logging
logging.info("User " + username + " logged in")  # G003: concatenation

