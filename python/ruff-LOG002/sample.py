# Sample for Ruff rule LOG002: invalid-get-logger-argument
# This file is designed to trigger the LOG002 rule.
# Run: ruff check --select LOG002 <this_file>

import logging
logger = logging.getLogger(__name__)
try:
    connect()
except Exception as e:
    logger.error("failed", exc_info=True)  # LOG002: use .exception()

