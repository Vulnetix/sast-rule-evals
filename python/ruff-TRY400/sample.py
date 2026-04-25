# Sample for Ruff rule TRY400: error-instead-of-exception
# This file is designed to trigger the TRY400 rule.
# Run: ruff check --select TRY400 <this_file>

import logging
try:
    connect()
except ConnectionError:
    logging.error("Connection failed")  # TRY400: use logging.exception

