# Sample for Ruff rule G004: logging-f-string
# This file is designed to trigger the G004 rule.
# Run: ruff check --select G004 <this_file>

import logging
logging.info(f"User {username} logged in")  # G004: f-string

