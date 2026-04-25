# Sample for Ruff rule G201: logging-exc-info
# This file is designed to trigger the G201 rule.
# Run: ruff check --select G201 <this_file>

import logging

try:
    ...
except ValueError:
    logging.error("Exception occurred", exc_info=True)
