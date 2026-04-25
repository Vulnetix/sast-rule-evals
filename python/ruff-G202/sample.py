# Sample for Ruff rule G202: logging-redundant-exc-info
# This file is designed to trigger the G202 rule.
# Run: ruff check --select G202 <this_file>

import logging

try:
    ...
except ValueError:
    logging.exception("Exception occurred", exc_info=True)
