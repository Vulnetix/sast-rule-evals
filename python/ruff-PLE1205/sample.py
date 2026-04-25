# Sample for Ruff rule PLE1205: logging-too-many-args
# This file is designed to trigger the PLE1205 rule.
# Run: ruff check --select PLE1205 <this_file>

import logging
logging.info("User %s has %d items", user)  # PLE1205: arg count mismatch

