# Sample for Ruff rule LOG015: root-logger-call
# This file is designed to trigger the LOG015 rule.
# Run: ruff check --select LOG015 <this_file>

import logging

logging.info("Foobar")
