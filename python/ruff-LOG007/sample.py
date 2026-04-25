# Sample for Ruff rule LOG007: exception-without-exc-info
# This file is designed to trigger the LOG007 rule.
# Run: ruff check --select LOG007 <this_file>

import logging
logging.exception("Something went wrong")  # LOG007: outside except block

