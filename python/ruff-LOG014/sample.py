# Sample for Ruff rule LOG014: exc-info-outside-except-handler
# This file is designed to trigger the LOG014 rule.
# Run: ruff check --select LOG014 <this_file>

import logging


logging.warning("Foobar", exc_info=True)
