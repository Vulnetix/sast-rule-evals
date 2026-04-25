# Sample for Ruff rule LOG004: log-exception-outside-except-handler
# This file is designed to trigger the LOG004 rule.
# Run: ruff check --select LOG004 <this_file>

import logging

logging.exception("Foobar")
