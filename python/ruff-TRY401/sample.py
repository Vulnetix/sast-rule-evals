# Sample for Ruff rule TRY401: verbose-log-message
# This file is designed to trigger the TRY401 rule.
# Run: ruff check --select TRY401 <this_file>

import logging
try:
    connect()
except Exception as e:
    logging.exception("failed", exc_info=True)  # TRY401: redundant exc_info

