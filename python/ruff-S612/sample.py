# Sample for Ruff rule S612: logging-config-insecure-listen
# This file is designed to trigger the S612 rule.
# Run: ruff check --select S612 <this_file>

import logging

logging.config.listen(9999)
